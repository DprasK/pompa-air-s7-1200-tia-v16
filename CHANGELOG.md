# Changelog

## 1.1.0 — 2026-09-01

- Menambahkan watch table `WT_Pump_Test` langsung ke proyek TIA Portal.
- Menambahkan 19 entri untuk I/O pompa, status, fault, feedback, dan preset waktu.
- Memperbarui arsip `.zap16`, validasi CRC/SHA-256, dokumentasi, dan bukti screenshot.

## 1.0.0 — 2026-09-01

- Menambahkan `FB_PumpControl_LAD [FB2]` dengan 53 network LAD.
- Mengubah `Main [OB1]` menjadi pemanggilan LAD ke FB2 melalui `DB_PumpControl_LAD [DB2]`.
- Menambahkan tabel `Pump_IO_LAD` dengan 13 tag I/O.
- Mempertahankan sumber SCL sebelumnya sebagai referensi offline.
- Memverifikasi Software rebuild all di TIA Portal V16 dengan 0 error dan 0 warning.
- Menambahkan validasi CRC arsip, manifest, bukti screenshot, dan workflow GitHub Actions.
