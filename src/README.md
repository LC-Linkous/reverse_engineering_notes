# src/ — Runnable Demos

Hands-on, **tool-usage** demos that go with the notes in the main
[README](../README.md) and the companion [demo ideas](../docs/SUPPLEMENTARY_NOTES.md#demo-ideas).
Each demo is a self-contained folder with its own `README.md` and, where it has
dependencies, a `requirements.txt`.

> **Hard guardrail for every demo:** owned devices, sanctioned course hardware,
> or signals that are legal to receive. No transmitting on restricted bands, no
> touching networks or devices you don't own, and no cloning of real access
> credentials or IDs. This mirrors the warnings in the main README.

## Available

| Demo | Topic | Gear | What it shows |
| ---- | ----- | ---- | ------------- |
| [`avr-firmware-extract/`](avr-firmware-extract/) | Hardware → Firmware | Two AVR boards (ArduinoISP) | Extract flash off an AVR you own, then convert and disassemble it into readable assembly. |
| [`serial-monitoring/`](serial-monitoring/) | Hardware → Serial | A USB-serial device | Three small serial monitors: one port, two ports (hardware + software serial), and a port scanner. |

More demos are planned across the four core topics (see the build plan in the
project TODO). Code here is licensed under **GPL-2.0** (see the repo
[LICENSE](../LICENSE)); the surrounding notes are CC-BY-SA-4.0.