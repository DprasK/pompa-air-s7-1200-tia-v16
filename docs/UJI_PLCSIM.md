# Panduan Uji PLCSIM — Pompa Air LAD

Uji ini belum dijalankan. Lakukan secara offline di TIA Portal V16/PLCSIM sebelum memakai PLC nyata.

## Persiapan

1. Retrieve `Pompa_Air_LAD_V16.zap16`.
2. Compile software dengan **rebuild all** dan pastikan 0 error.
3. Start PLCSIM untuk CPU 1214C yang dikonfigurasi; download hanya ke simulator.
4. Buat watch table untuk semua tag pada `IO_List.csv`, serta `DB_PumpControl_LAD`.State dan `.FaultBits`.
5. Untuk kondisi sehat awal, set `Pump_StopOK`, `Pump_SafetyOK`, `Pump_OverloadOK`, dan `Pump_SourceWaterOK` ke 1. Set feedback mengikuti command kecuali saat menguji fault.

## Skenario minimum

1. **Startup aman:** setelah restart, `Pump_PumpCmd=0`; tidak boleh start hanya karena level rendah.
2. **AUTO satu siklus:** set AUTO, tekan START sesaat, buat LowWet=0 dan HighWet=0. Setelah minimum OFF, command boleh ON. Set MotorFeedback=1 sebelum 3 s. Saat HighWet=1, command harus OFF.
3. **MANUAL satu siklus:** set MANUAL, tekan START sesaat. Pastikan command ON hanya bila semua permissive sehat dan minimum OFF terpenuhi; STOP membatalkan permintaan.
4. **Perubahan mode:** ubah AUTO/MANUAL saat berjalan. Command harus OFF dan operator harus memberi START baru.
5. **Minimum OFF:** setelah pompa OFF, berikan permintaan baru sebelum 5 s. Command harus tetap OFF sampai waktu minimum habis.
6. **Feedback hilang:** command ON tetapi pertahankan MotorFeedback=0 lebih dari 3 s. Alarm aktif dan FaultBits mengandung 32.
7. **Feedback tersangkut:** command OFF tetapi MotorFeedback tetap 1 lebih dari 3 s. Alarm aktif dan FaultBits mengandung 64.
8. **Maksimum runtime:** gunakan salinan uji dengan preset lebih pendek; command harus OFF dan FaultBits mengandung 16 setelah timeout.
9. **Interlock:** jatuhkan SafetyOK, OverloadOK, SourceWaterOK, atau StopOK saat berjalan. Command harus langsung OFF. Periksa fault terkait.
10. **Sensor mustahil:** set HighWet=1 dan LowWet=0. Alarm aktif dan FaultBits mengandung 8.
11. **Reset:** pulihkan penyebab fault lalu tekan RESET sesaat. Alarm dapat hilang, tetapi pompa tidak boleh restart sendiri.
12. **Preset invalid:** beri MinOffTime/FeedbackTime/MaxRunTime <= T#0s pada DB uji. FaultBits mengandung 128 dan command tidak boleh aktif.

Catat hasil setiap skenario, waktu aktual, State, FaultBits, dan screenshot trace/watch table. Jangan memaksa output fisik untuk pengujian ini.
