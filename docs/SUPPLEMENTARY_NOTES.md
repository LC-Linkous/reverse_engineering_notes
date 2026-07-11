# Supplementary Notes & Topic Backlog

> **Purpose of this file**
>
> This is a working "info dump" of topics, references, and demo ideas that aren't yet folded into the main README. It is intentionally over-inclusive — pull what you want into the course/public material and drop or trim the rest. Nothing here is required; treat it as a menu.

## Table of Contents

- [Legal & Ethics](#legal--ethics)
- [OSINT for Reverse Engineering](#osint-for-reverse-engineering)
- [FCC ID Lookups](#fcc-id-lookups)
- [Lab & VM Setup](#lab--vm-setup)
- [Computer / File-Format Notes](#computer--file-format-notes)
- [Vulnerabilities & Responsible Disclosure](#vulnerabilities--responsible-disclosure)
- [Practice Resources & CTFs](#practice-resources--ctfs)
- [Extended Reading List](#extended-reading-list)
- [Demo Ideas](#demo-ideas)

---

## Legal & Ethics

This is the single most important non-technical topic for a student audience, and worth a short dedicated section in the public material. Keep the tone "here is the landscape, talk to a lawyer for specifics" — laws vary by jurisdiction and change over time, and nothing here is legal advice.

**Key U.S. legal touchpoints (for awareness, not legal advice):**

- **DMCA §1201** — prohibits circumventing technological protection measures (e.g., DRM). The Library of Congress grants **triennial exemptions**, several of which cover good-faith security research, repair, and interoperability. The exemptions are narrow and conditional — the existence of an exemption does not make all research legal. (See the U.S. Copyright Office's §1201 rulemaking pages.)
- **Computer Fraud and Abuse Act (CFAA)** — the main U.S. anti-hacking statute. Centers on "access without authorization" / "exceeding authorized access." The takeaway for students: *authorization is everything.* Owning the device, or having written permission, is what separates research from a crime.
- **Wiretap Act / ECPA** — intercepting communications you aren't a party to (including some RF/network capture) can be illegal. Capturing your **own** traffic on your **own** network is the safe lane.
- **FCC regulations (Part 15, Part 97, etc.)** — govern RF transmission. Receiving is generally permissive; **transmitting** on licensed or restricted bands without authorization is not. Intentional jamming is specifically illegal.
- **Export controls (EAR/ITAR)** — relevant for some cryptographic and dual-use tooling; usually only matters at the professional/international level, but good to name.

**Ethics framing worth teaching:**

- **Scope and authorization first.** Written permission, defined targets, defined methods. "I owned it" or "I had permission, in writing, for exactly this" should be the default posture.
- **Minimize harm.** Don't degrade services others depend on; don't exfiltrate real personal data; prefer non-destructive methods unless destruction is justified and authorized.
- **Data handling.** If you incidentally capture someone's data, stop, document, and report — don't keep it.
- **Coordinated/responsible disclosure** over public "dropping." (Expanded below.)

**References to seed the section:**

- [U.S. Copyright Office — DMCA §1201 rulemaking](https://www.copyright.gov/1201/)
- [EFF — Coders' Rights Project](https://www.eff.org/issues/coders)
- [CISA — Coordinated Vulnerability Disclosure](https://www.cisa.gov/coordinated-vulnerability-disclosure-process)
- DOJ policy on good-faith security research under CFAA (2022 charging policy) — worth citing as it narrowed prosecution of good-faith research.

---

## OSINT for Reverse Engineering

Before touching a screwdriver, a surprising amount can be learned from public sources. This is cheap, non-destructive, and often the highest-value first step.

**What to look up and where:**

- **The device's own labels** → make, model, revision, serial scheme, regulatory IDs.
- **FCC ID** → internal photos, test reports, frequencies (see [FCC ID Lookups](#fcc-id-lookups)).
- **Component datasheets** → [Octopart](https://octopart.com/), [AllDatasheet](https://www.alldatasheet.com/), [Datasheets.com](https://www.datasheets.com/), manufacturer sites, [Digi-Key](https://www.digikey.com/) / [Mouser](https://www.mouser.com/) product pages.
- **Teardowns** → [iFixit](https://www.ifixit.com/Teardown), YouTube teardown channels, blogs. Someone may have already opened your exact device.
- **Firmware & manuals** → manufacturer support/download portals, [DD-WRT](https://dd-wrt.com/) / [OpenWrt](https://openwrt.org/) device pages for routers.
- **Regulatory/standards filings** → FCC, and for Europe the CE/RED documentation.
- **Patents** → [Google Patents](https://patents.google.com/) can reveal intended architecture and operation.
- **Code & issues** → GitHub/GitLab, vendor SDKs, support forums, and CVE databases ([NVD](https://nvd.nist.gov/), [MITRE CVE](https://cve.mitre.org/)).
- **Wireless registries** → Bluetooth SIG listings, WiFi Alliance certifications, Zigbee/CSA certifications.

**Why it matters:** a 20-minute search can tell you the SoC, the flash chip, the radio, the debug interface, and whether someone has already published a teardown or extracted the firmware — saving hours and avoiding unnecessary destructive steps.

---

## FCC ID Lookups

Any device legally sold in the U.S. with intentional RF emission carries an **FCC ID** (usually on the label: a grantee code + product code). It's one of the best beginner tricks.

**How to use it:**

1. Find the FCC ID on the device label (e.g., `2AB3C-XYZ123`).
2. Search the [official FCC ID database](https://www.fcc.gov/oet/ea/fccid) or a friendlier mirror like [fccid.io](https://fccid.io/).
3. Pull the **exhibits**, which frequently include:
   - **Internal photos** — see the PCB, chips, and layout without opening anything
   - **External photos** — label and port detail
   - **Test reports** — operating frequencies, power levels, modulation
   - **User manuals** and sometimes **block diagrams**
   - **Theory of operation** documents

**Teaching value:** it directly supports Component ID, PCB Layout, and Wireless Analysis, and it reinforces the "research before you disassemble" habit. A nice exercise: hand students a device, have them find the FCC ID, predict what's inside from the exhibits, then open it and compare.

---

## Lab & VM Setup

Reproducibility and isolation are the whole game. A short standardized setup section prevents a lot of pain (and a lot of accidental rule-breaking).

**Core principles:**

- **Isolate.** Analysis VMs should not have a path to production/lab infrastructure or to other students' machines. Use host-only or internal virtual networks. Treat any unknown binary/firmware as hostile.
- **Snapshot.** Take a clean snapshot before analysis and revert after. This makes runs reproducible and contains anything that misbehaves.
- **Reproduce.** Pin tool versions; record exact commands. Someone else following your notes should get the same result.
- **Never analyze hostile samples on shared infrastructure.** (This echoes the course's existing hard rules about the lab server.)

**Common building blocks:**

- **Hypervisors:** VirtualBox (free), VMware Workstation/Player, KVM/QEMU, Hyper-V.
- **Analysis distros:** [Kali Linux](https://www.kali.org/), [REMnux](https://remnux.org/) (malware-focused), [FlareVM](https://github.com/mandiant/flare-vm) (Windows RE toolset), [SIFT](https://www.sans.org/tools/sift-workstation/) (forensics).
- **Emulation:** QEMU for cross-architecture firmware/binaries; [Firmadyne](https://github.com/firmadyne/firmadyne)/[FAT](https://github.com/attify/firmware-analysis-toolkit) for router-style firmware.
- **Containers:** Docker for tool reproducibility (e.g., a pinned binwalk/EMBA image), but remember containers are weaker isolation than a VM for hostile code.
- **Networking discipline:** simulate the internet with [INetSim](https://www.inetsim.org/) or [FakeNet-NG](https://github.com/mandiant/flare-fakenet-ng) so a sample "phones home" into a sandbox, not the real network.

**Suggested student checklist:**

- [ ] Clean VM snapshot taken and named
- [ ] Network set to host-only / isolated
- [ ] Tool versions recorded in notes
- [ ] Shared folders are read-only (or off) for hostile samples
- [ ] Hashes recorded for any sample/firmware before and after
- [ ] Revert snapshot when done

---

## Computer / File-Format Notes

This fills the empty "Computer Notes" placeholder and bridges the hardware and code-analysis sections. The goal is just enough background to make a binary stop looking like noise.

**Identify before you analyze.** The first commands on any unknown blob:

- `file <blob>` — guesses type/architecture/endianness
- `binwalk <blob>` — scans for embedded signatures and filesystems
- `strings <blob>` (or FLOSS) — surfaces URLs, paths, version strings, hardcoded creds
- `xxd <blob> | head` / a hex editor — eyeball magic bytes and structure
- `binwalk --entropy <blob>` — high uniform entropy ≈ encrypted/compressed

**Executable formats (the big three):**

| Format | Platform | Magic | Notes |
| ------ | -------- | ----- | ----- |
| **ELF** | Linux/Unix, most embedded | `7F 45 4C 46` (`\x7FELF`) | Tools: `readelf`, `objdump`, Ghidra. Most IoT/router binaries. |
| **PE** | Windows (.exe/.dll) | `4D 5A` (`MZ`) | Tools: PEStudio, `pefile`, Ghidra/IDA. |
| **Mach-O** | macOS/iOS | `FE ED FA CE` / `CF` (and fat-binary `CA FE BA BE`) | Tools: `otool`, Hopper, Ghidra. |

**Concepts worth a paragraph each:**

- **Endianness** — byte order (big vs little). MIPS/ARM firmware can be either; getting it wrong makes everything look like garbage.
- **Architecture / ISA** — x86/x64, ARM (and Thumb), MIPS, RISC-V, AVR, etc. You must tell your disassembler the right one.
- **Memory layout** — code/text, data, stack, heap; why addresses matter when reading a disassembler.
- **Boot process** — bootloader → kernel → userspace; where firmware extraction can hook in (e.g., interrupting U-Boot over UART).
- **Filesystems in firmware** — SquashFS, JFFS2, CramFS, UBIFS, ext-family; binwalk/unblob carve these out.
- **Strings as a shortcut** — version banners, copyright lines, and config paths are often the fastest route to identifying components and finding CVEs.

---

## Vulnerabilities & Responsible Disclosure

The main README correctly keeps vuln-hunting out of scope, but a short "what to do if you stumble on one" section is responsible to include.

**The short version:**

- **Don't weaponize or hoard.** Finding a flaw isn't authorization to exploit it against others.
- **Document carefully.** Reproduction steps, affected versions, impact, and the environment.
- **Disclose coordinately.** Contact the vendor first (look for a `security.txt`, a `/security` page, or a bug-bounty program). Give them reasonable time to fix before any public discussion.
- **Use coordination bodies when stuck.** [CISA](https://www.cisa.gov/coordinated-vulnerability-disclosure-process) and [CERT/CC](https://www.kb.cert.org/vuls/) help mediate disclosure, especially for multi-vendor or unresponsive cases.
- **Hobby vs. professional differs.** As a hobbyist, a polite vendor email is the usual start. In a professional setting, follow your organization's disclosure policy and legal guidance.
- **Get a CVE** through a CNA when a fix or public advisory is warranted.

**Framing for students:** the goal of finding a vulnerability is to get it *fixed*, not to show off. Laws around disclosure vary by jurisdiction and are well outside the scope of course material — when in doubt, ask.

---

## Practice Resources & CTFs

Hands-on, legal targets where students can practice without touching anything they don't own.

**Reverse engineering / binary:**

- [crackmes.one](https://crackmes.one/) — community RE challenges, graded by difficulty
- [Microcorruption](https://microcorruption.com/) — browser-based embedded/MSP430 assembly CTF
- [pwn.college](https://pwn.college/) — free structured security curriculum (ASU)
- [OpenSecurityTraining2](https://ost2.fyi/) — deep free courses on architecture, RE, exploitation
- [Azeria Labs](https://azeria-labs.com/) — ARM assembly and exploitation tutorials
- [picoCTF](https://picoctf.org/) — beginner-friendly CTF with a persistent practice "gym"

**Web (high-level, sandboxed):**

- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — free, excellent, hosted labs
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) — deliberately vulnerable app you run yourself

**Hardware / wireless (mostly self-hosted or owned-device):**

- [OpenWrt](https://openwrt.org/) supported-device list — pick a cheap supported router as a safe firmware target
- SDR practice with [RTL-SDR](https://www.rtl-sdr.com/) on legal-to-receive signals (e.g., ADS-B aircraft, NOAA weather, your own devices)

> Keep the framing explicit for students: these exist precisely so you never need to practice on systems, networks, or devices you don't own or have permission to test.

---

## Extended Reading List

Beyond the main README's bookshelf:

**Books**

- *The Hardware Hacking Handbook* — van Woudenberg & O'Flynn (fault injection, side-channel, the deep end of hardware)
- *Practical IoT Hacking* — Chantzis et al. (broad, very hands-on, maps well to this repo's taxonomy)
- *Practical Reverse Engineering* — Dang, Gazet, Bachaalany (x86/x64/ARM, Windows internals, RE methodology)
- *The Ghidra Book* — Eagle & Nance
- *The IDA Pro Book* (2nd ed.) — Eagle
- *The Car Hacker's Handbook* — Smith (CAN bus, automotive — a fun applied domain)
- *The Art of Memory Forensics* — Ligh et al. (if forensics/memory comes up)
- *Practical Binary Analysis* — Andriesse (Linux/ELF, instrumentation, a great bridge to tooling)

**Sites / ongoing references**

- [Hackaday](https://hackaday.com/) — steady stream of teardowns and hardware hacks
- [Great Scott Gadgets](https://greatscottgadgets.com/) — HackRF/Ubertooth + tutorials
- [Osmocom](https://osmocom.org/) — open-source mobile/RF projects
- [PySDR](https://pysdr.org/) — SDR/DSP in Python
- [Ben Eater](https://eateror.com/) / YouTube — superb low-level digital/computer fundamentals

---

## Demo Ideas

Six to eight demos that map onto the four core topics, scale from "no special gear" to "lab gear," and stay firmly inside owned-device / legal boundaries. Each lists the topic, gear, the idea, and the learning objective. These are intended as **tool-usage demos**, consistent with the repo's "tools only" scope.

### 1. UART console drop on a cheap router (Hardware → Firmware)

- **Topic(s):** Physical Access, Circuit Investigation, Firmware
- **Gear:** A junk/owned router, USB-UART adapter (FTDI/CP2102), jumper wires, multimeter, `picocom`/`screen`.
- **Demo:** Find the UART header/pads (often a 4-pin row), identify GND/TX/RX with a multimeter and logic-level check, connect at a guessed baud (115200 is a good first try), and catch the boot log. Interrupt the bootloader to reach a U-Boot or busybox prompt.
- **Objective:** Students see a real serial console, learn pin identification and baud-rate hunting, and understand why a serial console is such a high-value foothold. Pure tool usage; nothing destructive.

### 2. Firmware carving with binwalk (Code → Firmware)

- **Topic(s):** Firmware, Computer/File-Format Notes
- **Gear:** A firmware image legally downloaded from a manufacturer's support site; a Linux VM with binwalk/unblob.
- **Demo:** Run `file`, then `binwalk` and `binwalk --entropy`, then extract the filesystem. Walk the extracted root: `etc/passwd`, hardcoded config, version strings via `strings`. Identify the architecture and one component you could look up a CVE for.
- **Objective:** Demystify "firmware" — show that an image is just packed filesystems + a kernel, and that triage tools reveal a lot fast. Reinforces the entropy → "is it encrypted?" intuition.

### 3. I2C/SPI sniffing with a logic analyzer (Hardware → Signal Analysis)

- **Topic(s):** Signal Analysis, Component ID
- **Gear:** A breakout sensor (e.g., an I2C temp sensor or EEPROM), microcontroller as the bus master, a cheap logic analyzer + PulseView (sigrok).
- **Demo:** Capture the bus, apply the I2C/SPI protocol decoder in PulseView, and read out the actual address + register traffic. Cross-reference decoded bytes against the sensor's datasheet.
- **Objective:** Connect the datasheet to the wire — students watch real protocol bytes and learn to use a logic analyzer's protocol decoders. Great Component-ID + Signal-Analysis combo.

### 4. BLE advertisement recon on your own wearable (Wireless → Bluetooth)

- **Topic(s):** Bluetooth/BLE, IoT Protocols
- **Gear:** A cheap owned BLE device (fitness band, beacon), a phone app (nRF Connect / LightBlue) and/or an nRF52840 dongle with the Wireshark BLE plugin.
- **Demo:** Scan for advertising packets, enumerate GATT services/characteristics, and observe what data the device broadcasts or exposes without pairing. Discuss what *should* and *shouldn't* be readable.
- **Objective:** Make the BLE attack surface concrete and low-cost, and surface the privacy lesson (devices that broadcast identifiers/data openly). Owned-device only.

### 5. ISM-band sensor decode with rtl_433 (Wireless → Sub-GHz/ISM)

- **Topic(s):** Sub-GHz/ISM, SDR basics
- **Gear:** An RTL-SDR dongle (receive-only) and `rtl_433`; a 433 MHz device you own (weather station, doorbell, TPMS in your own car, etc.).
- **Demo:** Run `rtl_433` and watch it auto-decode nearby ISM sensors into JSON. Discuss modulation (OOK/FSK) and why these protocols are often unauthenticated.
- **Objective:** A fully legal (receive-only) SDR win with instant gratification, teaching spectrum/sensor concepts and the "weak/no auth in ISM" theme without any transmission.

### 6. Local MQTT broker packet inspection (Network/IoT)

- **Topic(s):** IoT Protocols, Packet Capture, Protocol Analysis
- **Gear:** Mosquitto broker on a student workstation, a couple of publisher/subscriber scripts, Wireshark.
- **Demo:** Stand up a broker, publish/subscribe to topics, and capture the traffic in Wireshark using the MQTT dissector. Show plaintext payloads, then re-run with TLS and compare.
- **Objective:** Hands-on protocol analysis with zero hardware risk; demonstrates pub/sub mechanics and the concrete difference TLS makes. (The main README already notes MQTT is easy to self-host.)

### 7. APK static look with JADX (Code → Mobile)

- **Topic(s):** Mobile, Software
- **Gear:** An open-source / your-own APK, JADX (GUI), optionally apktool.
- **Demo:** Open the APK in JADX, browse decompiled Java, find the manifest's permissions and components, and locate strings like API endpoints or embedded config. Discuss what decompilation does and doesn't recover.
- **Objective:** Show mobile RE is approachable, reinforce decompiler limitations (lost names/comments), and connect to the OSINT/endpoint-discovery theme. Use only apps you're permitted to analyze.

### 8. RFID/NFC tag read with a phone or Proxmark (Wireless → RFID/NFC)

- **Topic(s):** RFID/NFC
- **Gear:** Blank/owned NFC tags, a smartphone (NFC Tools app) and/or a Proxmark3 for HF tags supplied for the exercise.
- **Demo:** Read tag UID and NDEF records, write a benign NDEF record to a blank tag, and read it back. With Proxmark, identify tag type and dump readable memory of a **course-provided** tag.
- **Objective:** Teach contactless basics and tag structure on sanctioned tags only.

> **Hard guardrail for every demo:** owned devices, sanctioned course hardware, or signals that are legal to receive. No transmitting on restricted bands, no touching networks/devices you don't own, and absolutely no cloning of real access credentials or IDs (this mirrors the warnings already in the main README).

---

### Quick mapping of demos to the four core topics

| Demo | Hardware | Code | Wireless | Network |
| ---- | :------: | :--: | :------: | :-----: |
| 1. UART console | ✅ | ✅ | | |
| 2. binwalk carving | | ✅ | | |
| 3. Logic-analyzer bus sniff | ✅ | | | |
| 4. BLE recon | | | ✅ | |
| 5. rtl_433 ISM decode | | | ✅ | |
| 6. MQTT inspection | | | ✅ | ✅ |
| 7. APK with JADX | | ✅ | | |
| 8. RFID/NFC read | | | ✅ | |