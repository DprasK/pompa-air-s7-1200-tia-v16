# Catatan Keselamatan

Program ini adalah contoh kontrol proses pada PLC standar S7-1200. Program tidak menggantikan fungsi keselamatan mesin dan tidak memiliki sertifikasi keselamatan fungsional.

- Emergency stop dan pemutusan energi berbahaya harus memakai rangkaian hardwired atau safety relay/F-CPU sesuai penilaian risiko.
- Proteksi overload motor harus tetap dapat memutus kontaktor tanpa bergantung pada program PLC standar.
- Proteksi dry-run, tekanan berlebih, kebocoran, dan level kritis harus dirancang sesuai bahaya instalasi nyata.
- `Pump_SafetyOK` hanya dipakai sebagai izin dan diagnostik program. Sinyal ini bukan satu-satunya lapisan keselamatan.
- Periksa logika fail-safe dari setiap sensor, jenis kontak NO/NC, tegangan I/O, dan kondisi kabel putus.
- Jalankan PLCSIM dan FAT terdokumentasi sebelum download ke PLC fisik.
- Saat commissioning, gunakan prosedur lockout/tagout dan personel yang kompeten.

Tidak ada download ke PLC fisik, perubahan RUN/STOP, atau uji PLCSIM yang dilakukan saat repository ini dibuat.

