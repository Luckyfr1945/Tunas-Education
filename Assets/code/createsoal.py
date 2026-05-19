import json

# Data soal bisa kamu ambil dari scraping, API, atau ketik langsung di sini
bank_soal = [
  {
    "teksPertanyaan": "Hewan pemakan daging disebut?",
    "pilihanJawaban": [
      "Herbivora",
      "Karnivora",
      "Omnivora",
      "Insektivora"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Bagian sel yang berfungsi sebagai pusat kendali seluruh aktivitas sel adalah?",
    "pilihanJawaban": [
      "Mitokondria",
      "Ribosom",
      "Nukleus",
      "Vakuola"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Proses pembuatan makanan pada tumbuhan dengan bantuan cahaya matahari disebut?",
    "pilihanJawaban": [
      "Respirasi",
      "Transpirasi",
      "Fotosintesis",
      "Fermentasi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Organ pada tumbuhan yang berfungsi menyerap air dan mineral dari tanah adalah?",
    "pilihanJawaban": [
      "Daun",
      "Batang",
      "Bunga",
      "Akar"
    ],
    "indeksJawabanBenar": 3
  },
  {
    "teksPertanyaan": "Hewan yang mengalami metamorfosis sempurna adalah?",
    "pilihanJawaban": [
      "Belalang",
      "Kecoa",
      "Kupu-kupu",
      "Jangkrik"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Zat hijau daun yang berperan dalam fotosintesis disebut?",
    "pilihanJawaban": [
      "Klorofil",
      "Karoten",
      "Antosianin",
      "Xantofil"
    ],
    "indeksJawabanBenar": 0
  },
  {
    "teksPertanyaan": "Organisme yang menguraikan sisa makhluk hidup menjadi zat anorganik disebut?",
    "pilihanJawaban": [
      "Produsen",
      "Konsumen",
      "Dekomposer",
      "Predator"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Bagian bunga yang menghasilkan serbuk sari adalah?",
    "pilihanJawaban": [
      "Putik",
      "Mahkota",
      "Benang sari",
      "Kelopak"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Jaringan pada tumbuhan yang berfungsi mengangkut air dari akar ke daun disebut?",
    "pilihanJawaban": [
      "Floem",
      "Xilem",
      "Epidermis",
      "Korteks"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Berikut ini yang termasuk hewan avertebrata (tidak bertulang belakang) adalah?",
    "pilihanJawaban": [
      "Ikan mas",
      "Katak",
      "Cacing tanah",
      "Ular"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Proses keluarnya keringat dari tubuh melalui pori-pori kulit merupakan fungsi kulit sebagai?",
    "pilihanJawaban": [
      "Alat ekskresi",
      "Alat reproduksi",
      "Alat respirasi",
      "Alat sirkulasi"
    ],
    "indeksJawabanBenar": 0
  },
  {
    "teksPertanyaan": "Hubungan antara dua makhluk hidup yang saling menguntungkan disebut?",
    "pilihanJawaban": [
      "Parasitisme",
      "Komensalisme",
      "Mutualisme",
      "Predasi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Sel darah merah pada manusia berfungsi untuk?",
    "pilihanJawaban": [
      "Membunuh kuman",
      "Mengangkut oksigen",
      "Pembekuan darah",
      "Menghasilkan antibodi"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Bagian mata yang mengatur banyak sedikitnya cahaya yang masuk adalah?",
    "pilihanJawaban": [
      "Kornea",
      "Lensa",
      "Iris",
      "Retina"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Tumbuhan yang berkembang biak dengan spora adalah?",
    "pilihanJawaban": [
      "Mangga",
      "Padi",
      "Pakis",
      "Kacang"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Ekosistem yang paling luas di permukaan bumi adalah?",
    "pilihanJawaban": [
      "Hutan hujan tropis",
      "Savana",
      "Ekosistem laut",
      "Padang rumput"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Virus berbeda dengan bakteri karena virus?",
    "pilihanJawaban": [
      "Bisa berkembang biak sendiri",
      "Memiliki sel",
      "Tidak memiliki inti sel dan hanya bisa hidup di dalam sel inang",
      "Bisa bergerak bebas"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Rantai makanan yang benar pada ekosistem sawah adalah?",
    "pilihanJawaban": [
      "Padi → Ular → Tikus → Elang",
      "Padi → Tikus → Ular → Elang",
      "Tikus → Padi → Ular → Elang",
      "Elang → Ular → Tikus → Padi"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Organ manusia yang menghasilkan insulin adalah?",
    "pilihanJawaban": [
      "Hati",
      "Lambung",
      "Pankreas",
      "Ginjal"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Tumbuhan yang dapat membuat makanan sendiri disebut?",
    "pilihanJawaban": [
      "Konsumen",
      "Dekomposer",
      "Autotrof",
      "Heterotrof"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Planet terdekat dengan Matahari adalah?",
    "pilihanJawaban": [
      "Venus",
      "Bumi",
      "Merkurius",
      "Mars"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Satuan kuat arus listrik dalam SI adalah?",
    "pilihanJawaban": [
      "Volt",
      "Ohm",
      "Ampere",
      "Watt"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Alat yang digunakan untuk mengukur massa benda adalah?",
    "pilihanJawaban": [
      "Termometer",
      "Barometer",
      "Neraca",
      "Dinamometer"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Bunyi yang frekuensinya di atas 20.000 Hz disebut?",
    "pilihanJawaban": [
      "Infrasonik",
      "Audiosonik",
      "Ultrasonik",
      "Supersonik"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Energi yang tersimpan pada benda yang berada di ketinggian tertentu disebut energi?",
    "pilihanJawaban": [
      "Kinetik",
      "Kimia",
      "Potensial gravitasi",
      "Mekanik"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Kecepatan cahaya di ruang hampa adalah?",
    "pilihanJawaban": [
      "300.000 km/s",
      "30.000 km/s",
      "3.000 km/s",
      "3.000.000 km/s"
    ],
    "indeksJawabanBenar": 0
  },
  {
    "teksPertanyaan": "Cermin yang digunakan pada kaca spion kendaraan adalah cermin?",
    "pilihanJawaban": [
      "Datar",
      "Cekung",
      "Cembung",
      "Prisma"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Hukum yang menyatakan bahwa setiap aksi menimbulkan reaksi yang sama besar tetapi berlawanan arah adalah Hukum Newton ke?",
    "pilihanJawaban": [
      "Pertama",
      "Kedua",
      "Ketiga",
      "Keempat"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Alat yang mengubah energi listrik menjadi energi gerak adalah?",
    "pilihanJawaban": [
      "Generator",
      "Dinamo",
      "Motor listrik",
      "Trafo"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Besaran yang memiliki nilai dan arah disebut besaran?",
    "pilihanJawaban": [
      "Skalar",
      "Vektor",
      "Turunan",
      "Pokok"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Benda yang dapat menghantarkan arus listrik dengan baik disebut?",
    "pilihanJawaban": [
      "Isolator",
      "Semikonduktor",
      "Konduktor",
      "Dielektrik"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Gaya tarik-menarik antara dua benda bermassa disebut gaya?",
    "pilihanJawaban": [
      "Gesek",
      "Normal",
      "Gravitasi",
      "Archimedes"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Alat yang digunakan untuk mengukur suhu adalah?",
    "pilihanJawaban": [
      "Barometer",
      "Termometer",
      "Higrometer",
      "Altimeter"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Peristiwa perubahan wujud dari cair ke gas disebut?",
    "pilihanJawaban": [
      "Membeku",
      "Menyublim",
      "Menguap",
      "Mengembun"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Gelombang yang membutuhkan medium untuk merambat disebut gelombang?",
    "pilihanJawaban": [
      "Elektromagnetik",
      "Mekanik",
      "Transversal",
      "Longitudinal"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Tekanan zat cair pada suatu titik bergantung pada?",
    "pilihanJawaban": [
      "Massa jenis dan luas permukaan",
      "Kedalaman dan massa jenis zat cair",
      "Volume dan suhu",
      "Luas dan volume"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Satuan energi dalam SI adalah?",
    "pilihanJawaban": [
      "Watt",
      "Newton",
      "Joule",
      "Pascal"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Peristiwa ikut bergetarnya suatu benda karena pengaruh benda lain yang bergetar dengan frekuensi sama disebut?",
    "pilihanJawaban": [
      "Difraksi",
      "Interferensi",
      "Resonansi",
      "Refleksi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Benda dikatakan dalam keseimbangan jika resultan gaya yang bekerja padanya adalah?",
    "pilihanJawaban": [
      "Maksimum",
      "Minimum",
      "Sama dengan nol",
      "Lebih besar dari nol"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Daya listrik diukur dalam satuan?",
    "pilihanJawaban": [
      "Ampere",
      "Volt",
      "Ohm",
      "Watt"
    ],
    "indeksJawabanBenar": 3
  },
  {
    "teksPertanyaan": "Lambang kimia untuk emas adalah?",
    "pilihanJawaban": [
      "Go",
      "Au",
      "Ag",
      "Ge"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Zat yang terbentuk dari dua unsur atau lebih yang bergabung secara kimia disebut?",
    "pilihanJawaban": [
      "Campuran",
      "Senyawa",
      "Larutan",
      "Koloid"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Larutan yang memiliki pH lebih dari 7 bersifat?",
    "pilihanJawaban": [
      "Asam",
      "Netral",
      "Basa",
      "Garam"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Rumus kimia air adalah?",
    "pilihanJawaban": [
      "CO2",
      "H2O",
      "NaCl",
      "O2"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Perubahan kimia yang terjadi saat kayu dibakar menghasilkan?",
    "pilihanJawaban": [
      "Zat yang sama",
      "Zat baru yang sifatnya berbeda",
      "Zat yang sama tapi berbeda bentuk",
      "Tidak menghasilkan zat baru"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Unsur yang paling banyak terdapat di kerak bumi adalah?",
    "pilihanJawaban": [
      "Besi",
      "Karbon",
      "Oksigen",
      "Silikon"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Proses pemisahan campuran berdasarkan perbedaan titik didih disebut?",
    "pilihanJawaban": [
      "Filtrasi",
      "Kristalisasi",
      "Destilasi",
      "Sublimasi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Ciri-ciri reaksi kimia yang ditandai dengan terbentuknya gas ditunjukkan oleh?",
    "pilihanJawaban": [
      "Perubahan warna",
      "Munculnya endapan",
      "Timbulnya gelembung",
      "Perubahan suhu"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Logam yang berwujud cair pada suhu ruangan adalah?",
    "pilihanJawaban": [
      "Besi",
      "Tembaga",
      "Merkuri (raksa)",
      "Aluminium"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Bahan yang digunakan sebagai indikator alami untuk menguji sifat asam-basa adalah?",
    "pilihanJawaban": [
      "Garam dapur",
      "Kunyit",
      "Tepung",
      "Minyak goreng"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Atom terdiri dari inti atom yang mengandung?",
    "pilihanJawaban": [
      "Proton dan elektron",
      "Elektron dan neutron",
      "Proton dan neutron",
      "Proton, neutron, dan elektron"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Perkaratan besi merupakan contoh reaksi kimia jenis?",
    "pilihanJawaban": [
      "Pembakaran",
      "Oksidasi",
      "Reduksi",
      "Fotosintesis"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Larutan yang nilai pH-nya 7 bersifat?",
    "pilihanJawaban": [
      "Asam kuat",
      "Basa kuat",
      "Netral",
      "Asam lemah"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Gas yang dihasilkan pada proses fotosintesis adalah?",
    "pilihanJawaban": [
      "Karbon dioksida",
      "Nitrogen",
      "Oksigen",
      "Hidrogen"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Lambang unsur natrium adalah?",
    "pilihanJawaban": [
      "Na",
      "Ni",
      "Ne",
      "N"
    ],
    "indeksJawabanBenar": 0
  },
  {
    "teksPertanyaan": "Campuran yang komponen-komponennya masih dapat dilihat secara kasat mata disebut campuran?",
    "pilihanJawaban": [
      "Homogen",
      "Koloid",
      "Heterogen",
      "Larutan"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Contoh perubahan fisika adalah?",
    "pilihanJawaban": [
      "Kayu terbakar",
      "Es mencair",
      "Besi berkarat",
      "Susu menjadi yoghurt"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Jumlah proton dalam inti atom menentukan?",
    "pilihanJawaban": [
      "Massa atom",
      "Nomor massa",
      "Nomor atom",
      "Isotop"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Asam yang terdapat dalam lambung manusia adalah?",
    "pilihanJawaban": [
      "Asam sulfat",
      "Asam sitrat",
      "Asam klorida",
      "Asam asetat"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Pemisahan campuran dengan cara menyaring menggunakan kertas saring disebut?",
    "pilihanJawaban": [
      "Destilasi",
      "Evaporasi",
      "Filtrasi",
      "Kromatografi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Lapisan atmosfer yang melindungi bumi dari sinar ultraviolet adalah?",
    "pilihanJawaban": [
      "Troposfer",
      "Mesosfer",
      "Ozonosfer (Stratosfer)",
      "Termosfer"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Gerhana matahari terjadi ketika?",
    "pilihanJawaban": [
      "Bumi berada di antara Matahari dan Bulan",
      "Bulan berada di antara Bumi dan Matahari",
      "Matahari berada di antara Bumi dan Bulan",
      "Bumi, Bulan, dan Matahari tidak segaris"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Lapisan bumi yang paling luar disebut?",
    "pilihanJawaban": [
      "Mantel",
      "Inti dalam",
      "Kerak bumi",
      "Inti luar"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Angin yang bertiup dari darat ke laut terjadi pada waktu?",
    "pilihanJawaban": [
      "Siang hari",
      "Malam hari",
      "Pagi hari",
      "Sore hari"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Benda langit yang mengelilingi planet disebut?",
    "pilihanJawaban": [
      "Komet",
      "Asteroid",
      "Satelit",
      "Meteor"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Planet yang memiliki cincin paling indah di tata surya adalah?",
    "pilihanJawaban": [
      "Jupiter",
      "Uranus",
      "Neptunus",
      "Saturnus"
    ],
    "indeksJawabanBenar": 3
  },
  {
    "teksPertanyaan": "Rotasi bumi menyebabkan terjadinya?",
    "pilihanJawaban": [
      "Pergantian musim",
      "Perbedaan lamanya siang dan malam",
      "Siang dan malam",
      "Gerhana bulan"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Fenomena alam yang disebabkan oleh pergerakan lempeng bumi adalah?",
    "pilihanJawaban": [
      "Hujan",
      "Gempa bumi",
      "Angin puting beliung",
      "Banjir"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Sumber energi utama bagi kehidupan di bumi adalah?",
    "pilihanJawaban": [
      "Bulan",
      "Angin",
      "Matahari",
      "Air"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Proses daur air yang mengubah air menjadi uap air disebut?",
    "pilihanJawaban": [
      "Kondensasi",
      "Presipitasi",
      "Evaporasi",
      "Infiltrasi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Batuan yang terbentuk dari magma yang membeku disebut batuan?",
    "pilihanJawaban": [
      "Sedimen",
      "Metamorf",
      "Beku",
      "Karbonat"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Alat yang digunakan untuk mengukur kekuatan gempa bumi adalah?",
    "pilihanJawaban": [
      "Barometer",
      "Anemometer",
      "Seismograf",
      "Termometer"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Planet terbesar dalam tata surya adalah?",
    "pilihanJawaban": [
      "Saturnus",
      "Uranus",
      "Neptunus",
      "Jupiter"
    ],
    "indeksJawabanBenar": 3
  },
  {
    "teksPertanyaan": "Curah hujan diukur dengan alat yang disebut?",
    "pilihanJawaban": [
      "Higrometer",
      "Anemometer",
      "Penakar hujan (Ombrometer)",
      "Barometer"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Pergerakan bumi mengelilingi matahari disebut?",
    "pilihanJawaban": [
      "Rotasi",
      "Presesi",
      "Revolusi",
      "Inklinasi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Organ yang berfungsi memompa darah ke seluruh tubuh adalah?",
    "pilihanJawaban": [
      "Paru-paru",
      "Ginjal",
      "Jantung",
      "Hati"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Proses pencernaan makanan pertama kali terjadi di?",
    "pilihanJawaban": [
      "Lambung",
      "Kerongkongan",
      "Rongga mulut",
      "Usus halus"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Enzim yang dihasilkan oleh lambung untuk memecah protein adalah?",
    "pilihanJawaban": [
      "Amilase",
      "Lipase",
      "Pepsin",
      "Tripsin"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Organ pernapasan yang berfungsi untuk pertukaran gas oksigen dan karbon dioksida adalah?",
    "pilihanJawaban": [
      "Hidung",
      "Tenggorokan",
      "Bronkus",
      "Alveolus"
    ],
    "indeksJawabanBenar": 3
  },
  {
    "teksPertanyaan": "Sistem saraf pusat terdiri dari?",
    "pilihanJawaban": [
      "Otak dan sumsum tulang belakang",
      "Otak dan saraf tepi",
      "Sumsum tulang belakang dan saraf otonom",
      "Saraf sensorik dan motorik"
    ],
    "indeksJawabanBenar": 0
  },
  {
    "teksPertanyaan": "Hormon yang mengatur kadar gula darah agar tetap normal adalah?",
    "pilihanJawaban": [
      "Adrenalin",
      "Tiroksin",
      "Insulin",
      "Estrogen"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Penyakit yang disebabkan oleh kekurangan vitamin C adalah?",
    "pilihanJawaban": [
      "Rakitis",
      "Beri-beri",
      "Skorbut",
      "Xeroftalmia"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Bagian ginjal yang berfungsi sebagai tempat penyaringan darah adalah?",
    "pilihanJawaban": [
      "Pelvis renalis",
      "Tubulus",
      "Glomerulus",
      "Ureter"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Tulang yang melindungi otak dari benturan adalah?",
    "pilihanJawaban": [
      "Tulang dada",
      "Tulang rusuk",
      "Tulang tengkorak",
      "Tulang belakang"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Penyakit tekanan darah tinggi disebut juga?",
    "pilihanJawaban": [
      "Anemia",
      "Hipertensi",
      "Diabetes",
      "Tifus"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Proses pengiriman sinyal dari indera ke otak dilakukan oleh saraf?",
    "pilihanJawaban": [
      "Motorik",
      "Otonom",
      "Sensorik",
      "Simpatik"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Kekurangan zat besi dalam tubuh dapat menyebabkan penyakit?",
    "pilihanJawaban": [
      "Diabetes",
      "Anemia",
      "Hipertensi",
      "Osteoporosis"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Proses masuknya udara ke paru-paru saat bernapas disebut?",
    "pilihanJawaban": [
      "Ekspirasi",
      "Difusi",
      "Inspirasi",
      "Oksigenasi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Sendi yang memungkinkan gerakan ke segala arah terdapat pada?",
    "pilihanJawaban": [
      "Lutut",
      "Siku",
      "Bahu",
      "Pergelangan kaki"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Zat sisa metabolisme yang dikeluarkan oleh ginjal dalam bentuk urin adalah?",
    "pilihanJawaban": [
      "Glukosa",
      "Protein",
      "Urea",
      "Lemak"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Energi yang dihasilkan dari reaksi kimia dalam sel tubuh disebut?",
    "pilihanJawaban": [
      "Energi kinetik",
      "Energi kimia",
      "Energi potensial",
      "Energi panas"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Getaran yang merambat disebut?",
    "pilihanJawaban": [
      "Frekuensi",
      "Amplitudo",
      "Gelombang",
      "Resonansi"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Tumbuhan yang menyimpan cadangan makanan di dalam umbi adalah?",
    "pilihanJawaban": [
      "Mangga",
      "Singkong",
      "Padi",
      "Jagung"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Alat yang berfungsi untuk memperbesar bayangan benda-benda yang sangat kecil disebut?",
    "pilihanJawaban": [
      "Teleskop",
      "Kamera",
      "Mikroskop",
      "Periskop"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Berikut ini yang merupakan sumber energi terbarukan adalah?",
    "pilihanJawaban": [
      "Batu bara",
      "Minyak bumi",
      "Gas alam",
      "Energi surya"
    ],
    "indeksJawabanBenar": 3
  },
  {
    "teksPertanyaan": "Pencemaran air dapat terjadi akibat pembuangan?",
    "pilihanJawaban": [
      "Daun kering",
      "Limbah industri",
      "Air hujan",
      "Pasir sungai"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Makhluk hidup bersel satu (uniseluler) yang menyebabkan penyakit malaria adalah?",
    "pilihanJawaban": [
      "Bakteri",
      "Virus",
      "Plasmodium",
      "Jamur"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Efek rumah kaca terjadi karena meningkatnya kadar gas?",
    "pilihanJawaban": [
      "Oksigen",
      "Nitrogen",
      "Karbon dioksida",
      "Hidrogen"
    ],
    "indeksJawabanBenar": 2
  },
  {
    "teksPertanyaan": "Tulang manusia tersusun dari mineral utama berupa?",
    "pilihanJawaban": [
      "Zat besi dan fosfor",
      "Kalsium dan fosfor",
      "Magnesium dan belerang",
      "Kalium dan natrium"
    ],
    "indeksJawabanBenar": 1
  },
  {
    "teksPertanyaan": "Proses pembelahan sel untuk pertumbuhan dan perbaikan jaringan disebut?",
    "pilihanJawaban": [
      "Meiosis",
      "Mitosis",
      "Fertilisasi",
      "Diferensiasi"
    ],
    "indeksJawabanBenar": 1
  }
]

# Unity butuh satu 'pembungkus' array utama biar gampang dibaca JsonUtility
data_export = {"kumpulanData": bank_soal}

with open("soal_ipa.json", "w", encoding="utf-8") as f:
    json.dump(data_export, f, indent=4)

print("File soal_ipa.json berhasil dibuat!")