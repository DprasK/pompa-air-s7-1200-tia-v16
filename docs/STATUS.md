# Status Validasi

- Arsip: `Pompa_Air_LAD_V16.zap16`
- Ukuran: 534835 byte
- SHA-256: `65a72e13ff16726609517d6af1e0a326627a98e8f811c0ebe68291ef2cf5d25f`
- Uji CRC ZIP/ZAP: **PASS** (60 entry, tidak ada entry rusak)
- TIA Portal V16 Software rebuild all: **0 error, 0 warning**
- Main OB1: **LAD**, memanggil FB2 dengan DB2
- FB2: **53 network LAD**
- Tabel I/O: **13 tag**, tanpa alamat ambigu
- PLCSIM: **belum dijalankan**
- PLC fisik: **tidak dihubungkan dan tidak di-download**

Hardware rebuild pada proyek referensi sebelumnya menghasilkan 0 error dan 1 warning terkait level proteksi CPU. Perlindungan akses harus ditentukan saat commissioning; warning tersebut bukan error program LAD.
