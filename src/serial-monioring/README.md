# Serial Monitoring

Three small, self-contained Python serial monitors — the everyday glue for
watching what a device says over UART/serial. Useful on their own, and handy
alongside the other demos (catching an Arduino's output, reading a boot log,
figuring out which port a device is on).

> **Scope / ground rules.** Point these at devices you own or are authorized to
> work with. They only *read* serial output; they don't transmit.

## Setup

Python 3 and the dependency in `requirements.txt`:

```
pip install -r requirements.txt
```

Serial **port names are machine-specific**: `COM5` on Windows,
`/dev/ttyUSB0` or `/dev/ttyACM0` on Linux, `/dev/tty.usbserial-XXXX` on macOS.
If you don't know which port your device is on, start with `loopCOM.py`.

## The three scripts

| Script | Use it when… | Example |
| ------ | ------------ | ------- |
| `readCOM.py` | you want to watch **one** port | `python readCOM.py --port COM5` |
| `twoCOM.py` | a board exposes **two** streams (e.g. hardware `Serial` over USB **and** a `SoftwareSerial`), and you want both, labeled | `python twoCOM.py --port1 COM5 --port2 COM26` |
| `loopCOM.py` | you **don't know the port** — it scans every port, reports which have data, and monitors the first active one | `python loopCOM.py` |

All three take `--baud` (default `9600`) and stop on `Ctrl-C`. Run any of them
with `--help` for the full options.

## Notes

- `readCOM.py` and `twoCOM.py` decode with `errors="replace"`, so a stray
  non-UTF-8 byte (common when the baud rate is wrong, or during a garbled boot
  banner) won't crash the monitor — you'll just see a replacement character.
- If you see nothing, the usual culprits are the wrong port or the wrong baud
  rate. `loopCOM.py` helps with the first; try common bauds (9600, 115200) for
  the second.

_Based on course materials for the reverse-engineering elective. Code is licensed under GPL-2.0 (see the repo [LICENSE](../../LICENSE))._