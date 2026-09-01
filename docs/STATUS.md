# Status Validasi

- Arsip: `Pompa_Air_LAD_V16.zap16`
- Ukuran: 521690 byte
- SHA-256: `85553ba576c54c7f4a11f501584312e1924d202a5d70ade4b36be1abf05909ac`
- Uji CRC ZIP/ZAP: **PASS** (50 entry, tidak ada entry rusak)
- Watch table: **WT_Pump_Test**, 19 entri, terdeteksi di dalam arsip
- TIA Portal V16 Software rebuild all: **0 error, 0 warning**
- Main OB1: **LAD**, memanggil FB2 dengan DB2
- FB2: **53 network LAD**
- Tabel I/O: **13 tag**, tanpa alamat ambigu
- PLCSIM: **belum dijalankan**
- PLC fisik: **tidak dihubungkan dan tidak di-download**

Hardware rebuild pada proyek referensi sebelumnya menghasilkan 0 error dan 1 warning terkait level proteksi CPU. Perlindungan akses harus ditentukan saat commissioning; warning tersebut bukan error program LAD.
