# Pompa Air S7-1200 — TIA Portal V16

Proyek kontrol pompa air sederhana berbasis **Ladder Diagram (LAD)** untuk **Siemens S7-1200 CPU 1214C DC/DC/DC** dan **S7-PLCSIM V16**.

## File proyek

- `Pompa_Air_LAD_V16.zap16` — arsip proyek native TIA Portal V16 yang dapat di-*retrieve* dan dimodifikasi.

## Cara membuka

1. Unduh `Pompa_Air_LAD_V16.zap16`.
2. Buka TIA Portal V16.
3. Pilih **Project > Retrieve**.
4. Pilih arsip tersebut, lalu tentukan folder tujuan.
5. Buka proyek hasil *retrieve*, lakukan **Compile > Software (rebuild all)**, lalu unduh ke S7-PLCSIM.

Jangan mencoba membuka atau mengedit isi `.zap16` secara langsung. Modifikasi dilakukan pada proyek hasil *retrieve*.

## I/O utama

| Alamat | Tag | Fungsi |
|---|---|---|
| `%I0.0` | `Pump_AutoMode` | Pilihan AUTO/MANUAL |
| `%I0.1` | `Pump_StartButton` | Tombol START |
| `%I0.2` | `Pump_StopOK` | Rangkaian STOP sehat |
| `%I0.3` | `Pump_SafetyOK` | Izin keselamatan |
| `%I0.4` | `Pump_OverloadOK` | Overload sehat |
| `%I0.5` | `Pump_SourceWaterOK` | Sumber air tersedia |
| `%I0.6` | `Pump_LowWet` | Sensor level rendah |
| `%I0.7` | `Pump_HighWet` | Sensor level tinggi |
| `%I1.0` | `Pump_ResetButton` | Reset alarm |
| `%I1.1` | `Pump_MotorFeedback` | Feedback motor |
| `%Q0.0` | `Pump_PumpCmd` | Perintah pompa |
| `%Q0.1` | `Pump_Alarm` | Alarm umum |
| `%Q0.2` | `Pump_Enabled` | Sistem siap |

## Uji dengan PLCSIM

Gunakan tabel simulasi atau watch table `WT_Pump_Test` untuk mengubah nilai input `%I`. Tidak perlu memakai **Force**. Output `%Q` hanya dimonitor karena nilainya dikendalikan oleh program PLC.

> Proyek ini hanya contoh pembelajaran. Untuk mesin nyata, gunakan rangkaian keselamatan, proteksi motor, penilaian risiko, dan prosedur commissioning yang sesuai.
