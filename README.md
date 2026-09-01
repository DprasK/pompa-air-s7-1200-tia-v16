# Pompa Air S7-1200 — TIA Portal V16 (LAD)

Proyek kontrol pompa air untuk **Siemens S7-1200 CPU 1214C DC/DC/DC** (`6ES7 214-1AG40-0XB0`, firmware 4.4). Program utama menggunakan Ladder Diagram (LAD) dan telah dikompilasi di TIA Portal V16.

> [!WARNING]
> Proyek ini bukan program F-CPU atau fungsi keselamatan bersertifikat. Baca [dokumen keselamatan](docs/SAFETY.md) sebelum simulasi atau commissioning.

## Hasil validasi

| Pemeriksaan | Hasil |
|---|---:|
| TIA Portal V16 — Software rebuild all | 0 error, 0 warning |
| FB LAD | 53 network |
| Tabel I/O | 13 tag |
| CRC arsip `.zap16` | Lulus, 60 entry |
| Uji diferensial logika | 61.024 scan |
| Perbandingan wiring XML | 12.000 scan |
| PLCSIM / PLC fisik | Belum dijalankan |

## Struktur program

- `Main [OB1]` dalam LAD memanggil `FB_PumpControl_LAD [FB2]`.
- `DB_PumpControl_LAD [DB2]` menjadi instance DB untuk FB2.
- `Pump_IO_LAD` berisi alamat I/O tetap.
- Blok SCL lama disimpan di `source/reference_scl/` sebagai referensi dan tidak dipanggil oleh OB1.

## Menggunakan proyek

1. Unduh [project/Pompa_Air_LAD_V16.zap16](project/Pompa_Air_LAD_V16.zap16).
2. Di TIA Portal V16, pilih **Project > Retrieve**.
3. Pilih arsip tersebut dan tentukan folder tujuan lokal.
4. Jalankan **Compile > Software (rebuild all)**.
5. Periksa konfigurasi CPU, alamat I/O, wiring, proteksi akses, dan interlock sebelum download.
6. Ikuti [panduan uji PLCSIM](docs/UJI_PLCSIM.md).

Ekstensi `.ap16` adalah bagian dari folder proyek TIA dan tidak boleh dipindahkan sendiri. Arsip `.zap16` dipakai agar seluruh proyek dapat dipindahkan dan di-*retrieve* dengan benar. File `.als16` tidak diperlukan karena proyek ini standalone, bukan sesi Multiuser.

## I/O

Daftar lengkap tersedia di [docs/IO_List.csv](docs/IO_List.csv).

| Alamat | Tag | Fungsi |
|---|---|---|
| `%I0.0` | `Pump_AutoMode` | Pemilihan AUTO/MANUAL |
| `%I0.1` | `Pump_StartButton` | Tombol START |
| `%I0.2` | `Pump_StopOK` | Rangkaian STOP sehat |
| `%I0.3` | `Pump_SafetyOK` | Izin keselamatan |
| `%I0.4` | `Pump_OverloadOK` | Kontak overload sehat |
| `%I0.5` | `Pump_SourceWaterOK` | Sumber air tersedia |
| `%I0.6` | `Pump_LowWet` | Sensor level rendah |
| `%I0.7` | `Pump_HighWet` | Sensor level tinggi |
| `%I1.0` | `Pump_ResetButton` | Reset alarm |
| `%I1.1` | `Pump_MotorFeedback` | Feedback kontaktor/motor |
| `%Q0.0` | `Pump_PumpCmd` | Perintah kontaktor pompa |
| `%Q0.1` | `Pump_Alarm` | Alarm umum |
| `%Q0.2` | `Pump_Enabled` | Kontrol siap |

## Isi repository

- `project/`: arsip native TIA Portal V16.
- `source/`: XML VCI LAD dan sumber SCL referensi.
- `docs/`: daftar I/O, status, keselamatan, dan rencana uji PLCSIM.
- `validation/`: manifest hasil pemeriksaan dan screenshot TIA Portal.
- `tools/validate_delivery.py`: pemeriksaan lokal/CI tanpa dependensi eksternal.

Jalankan validasi repository dengan:

```powershell
python tools/validate_delivery.py
```

