# Hasil Uji S7-PLCSIM

Tanggal: 2 September 2026  
Target: S7-1200 CPU 1214C DC/DC/DC di S7-PLCSIM/TIA Portal V16  
Program: `Main [OB1]` LAD, `FB_PumpControl_LAD [FB2]`, dan `DB_PumpControl_LAD [DB2]`

## Hasil

| Skenario | Input/kondisi utama | Hasil yang diamati | Status |
|---|---|---|---:|
| Reset sehat | Stop, safety, overload, dan sumber air sehat; motor berhenti; pulsa reset | `State=0`, `FaultBits=16#0000`, alarm OFF, command OFF | PASS |
| AUTO running | AUTO, level rendah, pulsa START, feedback motor ON | `State=40`, `PumpCmd=TRUE`, `Enabled=TRUE`, `RunningConfirmed=TRUE`, `FaultBits=16#0000` | PASS |
| Stop level tinggi | `LowWet=TRUE`, `HighWet=TRUE`, feedback motor OFF | `State=10`, `PumpCmd=FALSE`, alarm OFF, `FaultBits=16#0000` | PASS |
| Fault sumber air | `SourceWaterOK=FALSE` | `State=90`, alarm ON, `FaultBits=16#0004`, command OFF | PASS |

## Metode simulator

Penulisan satu kali dan forcing alamat `%I` pada instance PLCSIM ini tidak diteruskan ke process image input. Untuk menguji logika FB secara deterministik, sepuluh tag input pada proyek kerja simulator dipetakan sementara ke memory bit non-retentif `%M10.0`–`%M11.1`. `FeedbackTime` juga dinaikkan sementara agar kontrol GUI otomatis dapat memberikan feedback sebelum timeout.

Setelah uji, proyek kerja dikembalikan ke alamat fisik `%I0.0`–`%I1.1`, `FeedbackTime=T#3s`, dan berhasil dimuat kembali ke PLCSIM. Tidak ada force aktif dan CPU simulator ditinggalkan pada mode STOP. Arsip rilis `.zap16` tidak pernah diubah ke pemetaan memory bit.

## Bukti

- `PLCSIM_01_Reset_Clear.png`
- `PLCSIM_02_Auto_Running.png`
- `PLCSIM_03_High_Level_Stop.png`
- `PLCSIM_04_Source_Fault.png`
- `PLCSIM_05_Final_Safe_Stop.png`

Pengujian ini memvalidasi perilaku program pada simulator. Wiring lapangan, kontaktor, proteksi motor, sensor, dan rangkaian keselamatan tetap memerlukan commissioning pada instalasi sebenarnya.
