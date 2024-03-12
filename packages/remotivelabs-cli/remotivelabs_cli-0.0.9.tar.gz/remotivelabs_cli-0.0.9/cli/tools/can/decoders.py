import os.path
from typing import Union

import can
import cantools
from can import Message as CanMessage
from cantools.database import Database, Message
from cantools.database.errors import DecodeError
from cantools.database.namedsignalvalue import NamedSignalValue
from cantools.typechecking import DecodeResultType


class CanDecoder:
    def __init__(self, signal_db_path: str, namespace: str = None):
        self.signal_db: Union[Database, Database] = cantools.database.load_file(signal_db_path)
        self.signal_db_path = signal_db_path
        self.failed_arb_id = list()
        self.successful_arb_id = list()
        self.namespace = namespace

    def decode_log_file_legacy(self, filename: str):
        file1 = open(filename, "r")
        Lines = file1.readlines()
        return list(map(self.decode_log_line, Lines))

    def decode_log_file(self, filename):
        with can.LogReader(filename) as reader:
            return list(map(self.__do_decode, reader))

    def decode_log_line(self, line: str):
        try:
            time_ns_rawframe = line.split(" ")
            ts = float(time_ns_rawframe[0][1:18])
            ns = time_ns_rawframe[1]
            rawframe = time_ns_rawframe[2]
            arbid_and_data = rawframe.split("#")
            arb_id = int(arbid_and_data[0], 16)

            frame_infos = list(filter(lambda m: m.frame_id == arb_id, self.signal_db.messages))

            if len(frame_infos) == 0:
                return None

            # message('PHEV_Battery_Data1_HS3', 0x3d4, False, 8, None)
            frame_info: Message = frame_infos[0]

            data = bytes.fromhex(arbid_and_data[1])
            # print(frame)
            # print(frame.name)
        except Exception as e:
            print(e)
            return None

        try:
            # {'BattTracSoc_Pc_Dpltd': 4.5}
            signal: DecodeResultType = self.signal_db.decode_message(arb_id, data)
            # if frame_info.name == 'TransGearData_HS1':
            #    for s in list(signal):
            #        print(f"signal {s} - {signal[s].value} - {type(signal[s])}")

            def signal_value(some_signal_value):
                # NamedSignalValue contains name: int pair where "name" is the
                # explanation or str version of the int from my understanding
                # Sample from dbc file
                #
                # SignalName
                # 0 AutonomousBrkPedalMove
                # 1 NoAutonomousBrkPdlMovement
                # 2 DriverApplyingBrakePedal
                # 3 Unknown
                if isinstance(some_signal_value, NamedSignalValue):
                    return some_signal_value.value
                else:
                    return some_signal_value

            all_signals = map(lambda m: {"type": type(signal[m]).__name__, "name": m, "value": signal_value(signal[m])}, list(signal))
            numeric_signals_kv = list(filter(lambda m: type(m["value"]) is float or type(m["value"]) is int, all_signals))

            self.successful_arb_id.append(arb_id)
            return {
                "name": frame_info.name,
                "timestamp": ts,
                "signal_db": os.path.basename(self.signal_db_path),
                "namespace": ns,
                "signals": list(numeric_signals_kv),
            }

        except KeyError as e:
            print(e)
            # print(f"Failed to parse msg for {arb_id} {str(e)}")
            self.failed_arb_id.append(arb_id)
            return

        except Exception as e:
            print(e)
            self.failed_arb_id.append(arb_id)
            return
            # print(f"EX: Failed to parse msg for {arb_id}  + {str(ex)}")
            # print(str(e))

    def decode_asc_file(self, filename, **kwargs):
        logfile = os.path.join(os.path.dirname(__file__), "data", filename)
        print(logfile)

        with can.ASCReader(filename, "hex", False, **kwargs) as reader:
            return list(map(self.__do_decode, reader))

    def asc2blf(self, asc_file, blf_file, **kwargs):
        with open(asc_file, "r") as f_in:
            log_in = can.io.ASCReader(f_in, "hex", False)

            with open(blf_file, "wb") as f_out:
                log_out = can.io.BLFWriter(f_out)
                for msg in log_in:
                    log_out.on_message_received(msg)
                log_out.stop()

    def log2asc(self, log_file, asc_file, **kwargs):
        with can.LogReader(log_file) as log_in:
            with open(asc_file, "w") as f_out:
                log_out = can.io.ASCWriter(f_out)
                for msg in log_in:
                    log_out.on_message_received(msg)
                log_out.stop()

    def decode_blf_file(self, filename, **kwargs):
        logfile = os.path.join(os.path.dirname(__file__), "data", filename)
        print(logfile)
        with can.BLFReader(filename, **kwargs) as reader:
            return list(map(self.__do_decode, reader))

    def __do_decode(self, mesg: CanMessage):
        try:
            signal: DecodeResultType = self.signal_db.decode_message(mesg.arbitration_id, mesg.data)
            message = self.signal_db.get_message_by_frame_id(mesg.arbitration_id)
            numeric_signals_kv = list(
                filter(
                    lambda m: type(m["value"]) is float or type(m["value"]) is int,
                    map(lambda m: {"name": m, "value": signal[m]}, list(signal)),
                )
            )
            self.successful_arb_id.append(mesg.arbitration_id)
            return {
                "name": message.name,
                "timestamp": mesg.timestamp,
                "signal_db": os.path.basename(self.signal_db_path),
                "namespace": self.namespace,
                "signals": list(numeric_signals_kv),
            }
        except KeyError:
            # print(e)
            self.failed_arb_id.append(mesg.arbitration_id)
            return None

        except DecodeError:
            # print(e)
            self.failed_arb_id.append(mesg.arbitration_id)
            return None
        except Exception:
            # print(e)
            self.failed_arb_id.append(mesg.arbitration_id)
            return None
