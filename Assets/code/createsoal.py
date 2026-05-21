import json

# Data soal bisa kamu ambil dari scraping, API, atau ketik langsung di sini
bank_soal = [
    {
        "teksPertanyaan": "Seseorang datang ke kondangan dengan baju super heboh mengalahkan pengantin. Reaksi sarkas yang paling tepat adalah?",
        "pilihanJawaban": [
            "Baju kamu bagus sekali, beli di mana?",
            "Mohon maaf, ini yang mau nikah sebenarnya kamu atau pengantinnya?",
            "Wah, gaunnya sederhana sekali ya, hampir tidak kelihatan.",
            "Besok-besok kalau ke kondangan pakai kaos oblong saja."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu hobi pamer motor baru tapi ternyata cicilannya macet 6 bulan. Kalimat sindiran yang pas adalah?",
        "pilihanJawaban": [
            "Gaya elit, bayar cicilan sulit.",
            "Wah, motornya keren banget, pasti cash ya?",
            "Besok beli mobil baru lagi dong!",
            "Hebat, kamu pintar mengatur keuangan."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Saat melihat jalan raya di Indonesia yang lubangnya sedalam kolam lele, ucapan sarkas netizen biasanya?",
        "pilihanJawaban": [
            "Jalanan ini sangat mulus seperti perosotan.",
            "Wah, pemerintah kreatif ya, bikin fasilitas kolam renang gratis di jalan.",
            "Duh, jalannya rusak banget, harus segera diperbaiki.",
            "Untung saya naik tank, jadi aman."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu janji datang jam 7 malam, tapi baru muncul jam 10 malam. Kalimat menyambutnya yang paling sarkas adalah?",
        "pilihanJawaban": [
            "Kenapa kamu telat sekali?",
            "Wah, kamu datang terlalu cepat, acara besok pagi belum mulai.",
            "Makasih ya sudah menyempatkan datang.",
            "Besok-besok kita kumpul jam 10 saja."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Seseorang membuang sampah sembarangan tepat di bawah papan larangan membuang sampah. Sindiran yang tepat adalah?",
        "pilihanJawaban": [
            "Wah, kamu buta huruf ya?",
            "Mungkin papan larangannya kurang besar teksnya.",
            "Keren, tingkatkan terus bakat merusak alamnya ya!",
            "Jangan buang sampah di sini, nanti didenda."
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Ketika ada pejabat yang mendadak sering blusukan dan bagi-bagi sembako, itu tandanya?",
        "pilihanJawaban": [
            "Beliau sudah bertobat",
            "Pemilu sudah dekat",
            "Sembakonya mau kedaluwarsa",
            "Beliau sedang gabut"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu merasa paling tahu segalanya dan tidak mau kalah saat berargumen. Julukan sarkas netizen untuknya adalah?",
        "pilihanJawaban": [
            "Profesor",
            "Maha Benar Netizen dengan Segala Firmannya",
            "Si Paling Benar",
            "Kamus Berjalan"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Melihat orang yang sibuk merekam kecelakaan jalan raya demi konten daripada menolong korban. Sindiran yang pas adalah?",
        "pilihanJawaban": [
            "Kameranya bagus, berapa megapixel?",
            "Semoga dapet banyak viewer ya, nyawa orang kan nomor dua.",
            "Tolong rekam dari angle yang lebih dekat lagi.",
            "Wah, kamu berbakat jadi jurnalis."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Internet di rumahmu sangat lambat sampai-sampai membuka Google saja butuh waktu 10 menit. Ucapan sarkasnya?",
        "pilihanJawaban": [
            "Provider ini sangat lambat.",
            "Saking cepatnya internet ini, saya bisa ditinggal tidur siang.",
            "Internetnya stabil banget, stabil lemotnya.",
            "Saya harus ganti provider bulan depan."
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Ada orang awam yang hobi menceramahi dokter ahli tentang kesehatan bermodalkan artikel WhatsApp. Istilah sarkasnya?",
        "pilihanJawaban": [
            "Si Paling Dokter",
            "Lulusan Universitas Google",
            "Pakar Kesehatan Internasional",
            "Saksi Hidup Kebenaran"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat seseorang mengantre lalu barisannya diserobot oleh emak-emak, reaksi pasrah nan sarkas adalah?",
        "pilihanJawaban": [
            "Silakan bu, antrean ini memang milik ras terkuat di bumi.",
            "Hei, jangan menyerobot antrean saya!",
            "Ibu mau saya panggilkan polisi?",
            "Wah, ibu buru-buru ya? Mau ke mana?"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Temanmu meminjam uang dengan memelas, tapi saat ditagih dia malah lebih galak dari kamu. Fenomena ini disebut?",
        "pilihanJawaban": [
            "Hukum Utang-Piutang Indonesia",
            "Sifat manusia purba",
            "Amor fati",
            "Keajaiban dunia kedelapan"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Ketika cuaca di luar rumah sangat panas menyengat hingga mencapai 38 derajat Celcius, respons sarkasnya adalah?",
        "pilihanJawaban": [
            "Hari ini panas sekali.",
            "Mataharinya lagi ditaruh di atas kepala ya?",
            "Ini bumi atau simulasi neraka bocor ya?",
            "Wah, jemuran saya pasti cepat kering."
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Ada akun media sosial yang hobinya memamerkan kekayaan hasil korupsi atau nipu orang. Komentar netizen biasanya?",
        "pilihanJawaban": [
            "Ditunggu baju orange-nya ya kak!",
            "Wah, sukses terus ya usahanya!",
            "Bagi-bagi dong uangnya.",
            "Minimal sedekah dulu biar berkah."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Kamu mengerjakan tugas kelompok sendirian, tapi semua anggota minta ditulis namanya di lembar jawaban. Kalimat sindiranmu?",
        "pilihanJawaban": [
            "Kalian malas sekali.",
            "Terima kasih ya atas doa dan dukungannya, sangat membantu.",
            "Besok-besok jangan sekelompok sama saya lagi.",
            "Nanti saya laporkan ke dosen ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu mengeluh tidak punya uang buat makan, tapi besoknya dia pamer nonton konser VIP. Respons kamu?",
        "pilihanJawaban": [
            "Katanya kemarin miskin?",
            "Wah, dapet sumbangan dari mana tuh?",
            "Kemiskinanmu sangat estetik dan fleksibel ya.",
            "Bagi tiketnya dong satu."
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Melihat orang yang motornya pakai knalpot brong bising luar biasa tapi jalannya pelan. Sindiran yang pas?",
        "pilihanJawaban": [
            "Suara motornya kayak helikopter tempur, tapi jalannya kayak siput.",
            "Knalpotnya merusak telinga orang.",
            "Mas, motornya rusak ya kok suaranya begitu?",
            "Keren banget mas motornya, beli di mana?"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Istilah netizen untuk mengomentari orang yang sering pamer kemewahan yang ternyata palsu atau hasil sewaan adalah?",
        "pilihanJawaban": [
            "Crazy Rich Asli",
            "Flexing Elit, Ekonomi Sulit",
            "Pengusaha Sukses",
            "Sultan Palsu"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika lowongan kerja syaratnya: S1, pengalaman 5 tahun, menguasai 10 keahlian, tapi gajinya UMR. Komentar pelamar kerja?",
        "pilihanJawaban": [
            "Ini perusahaan pelit.",
            "Dicari: Karyawan berjiwa Avengers dengan gaji magang.",
            "Saya tidak tertarik melamar di sini.",
            "Persyaratannya terlalu mudah bagi saya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu baru putus 2 jam yang lalu, tapi status WhatsApp-nya sudah pasang foto sama pacar baru. Sindiran yang pas?",
        "pilihanJawaban": [
            "Cepat amat dapet penggantinya.",
            "Wah, hatimu pakai sistem fast charging ya?",
            "Selamat ya atas hubungan barunya.",
            "Mantanmu pasti menangis melihat ini."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat melihat tumpukan berkas administrasi di kantor pemerintahan yang masih pakai kertas padahal jargonnya 'Digitalisasi'. Komentar sarkasnya?",
        "pilihanJawaban": [
            "Sangat ramah lingkungan.",
            "Digitalisasi berbasis tebang pohon.",
            "Hebat, arsipnya rapi sekali.",
            "Sistemnya modern sekali ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Seorang cowok berjanji akan membelikan ceweknya pulau, tapi buat bayar parkir Rp2.000 saja pura-pura dompetnya ketinggalan. Sarkas yang pas?",
        "pilihanJawaban": [
            "Janji manismu setinggi langit, dompetmu setipis tisu.",
            "Pulau yang mau dibeli mungkin pulau kapuk.",
            "Kamu pelit banget sih jadi cowok.",
            "Uang parkirnya biar aku yang bayar aja."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang kerjaannya komentar negatif dan menghujat semua postingan orang lain tanpa alasan. Netizen menyebutnya?",
        "pilihanJawaban": [
            "Kritikus Seni",
            "Penduduk Asli Twitter",
            "Manusia Tanpa Beban Dosa",
            "Pengacara Kehidupan"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Melihat ruangan kelas atau kantor yang AC-nya rusak sampai semua orang mandi keringat. Ucapan sarkasnya?",
        "pilihanJawaban": [
            "Fasilitas di sini sangat buruk.",
            "Wah, asyik ya, ruangan ini merangkap jadi ruang sauna gratis.",
            "Tolong panggil tukang servis AC.",
            "Gak apa-apa, biar sehat bakar lemak."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu memotong pembicaraanmu terus-menerus karena ingin menceritakan dirinya sendiri. Kalimat sindiranmu?",
        "pilihanJawaban": [
            "Bisa diam sebentar tidak?",
            "Maaf ya saya lancang mendengarkan kamu berbicara.",
            "Silakan lanjut ceritanya, panggung ini milikmu.",
            "Kamu egois sekali ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika ada aturan baru yang bikin masyarakat makin susah tapi judul aturannya 'Demi Kesejahteraan Rakyat'. Respons masyarakat?",
        "pilihanJawaban": [
            "Terima kasih, kami merasa sangat disejahterakan hingga sesak napas.",
            "Aturan ini harus segera dicabut.",
            "Pemerintah selalu memikirkan rakyatnya.",
            "Mari kita demo ke jalanan."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Seseorang mengunggah foto selfie dengan wajah penuh filter ekstrem sampai pagar di latar belakangnya ikut meliuk. Komentar sarkasnya?",
        "pilihanJawaban": [
            "Cantik/ganteng banget kak!",
            "Fotonya estetik, pagarnya sampai insecure dan ikutan insecure.",
            "Filternya ketebalan itu kak.",
            "Bisa ajarkan cara edit fotonya?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Teman kelompokmu tidak bekerja sama sekali tapi saat presentasi dia yang paling banyak bicara di depan guru. Dia pantas dijuluki?",
        "pilihanJawaban": [
            "Ketua Kelompok Idaman",
            "Seksi Humas Gaib",
            "Menteri Penerangan Dadakan",
            "Parasit Berbakat"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Ketika lampu lalu lintas baru berubah warna hijau 0,001 detik, tapi pengendara di belakangmu sudah klakson bertubi-tubi. Istilah untuk mereka?",
        "pilihanJawaban": [
            "Pembalap Formula 1",
            "Duta Klakson Indonesia",
            "Orang yang besok mau kiamat",
            "Pengendara disiplin"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Kamu sedang diet ketat, tapi temanmu terus-menerus mengirimkan foto makanan enak jam 12 malam. Kalimat balasan sarkasmu?",
        "pilihanJawaban": [
            "Jangan kirim itu, aku lagi diet.",
            "Terima kasih ya, pahala kamu mengalir deras dari penderitaanku.",
            "Wah, makanannya kelihatan lezat sekali.",
            "Besok temani aku beli makanan itu ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Seorang influencer membuat video minta maaf setelah ketahuan berbuat salah, tapi ekspresinya datar seperti membaca teks proklamasi. Komentar netizen?",
        "pilihanJawaban": [
            "Permintaan maafnya sangat tulus.",
            "Aktingnya kurang dapet, besok coba pakai nangis ya.",
            "Saya sudah memaafkan kamu.",
            "Semoga ini menjadi pelajaran."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat harga telur dan minyak goreng naik melambung tinggi, reaksi ibu-ibu yang sarkas adalah?",
        "pilihanJawaban": [
            "Wah, besok kita makan angin saja yang masih gratis.",
            "Uang belanja dari suami harus ditambah nih.",
            "Pemerintah tolong turunkan harga pangan.",
            "Gak apa-apa, sekalian diet kolesterol."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Temanmu berjanji mengembalikan uangmu 'besok', tapi sudah lewat 3 tahun belum dibayar juga. Arti kata 'besok' bagi dia adalah?",
        "pilihanJawaban": [
            "Hari setelah hari ini",
            "Saat negara api menyerang",
            "Ketika dia sudah kaya raya",
            "Abadi tanpa batas waktu"
        ],
        "indeksJawabanBenar": 3
    },
    {
        "teksPertanyaan": "Saat banjir menggenangi rumah warga hingga sepinggang, komentar pasrah warga ke kamera berita biasanya?",
        "pilihanJawaban": [
            "Rumah kami hancur, kami sedih.",
            "Lumayan dapet fasilitas Waterboom gratis tahunan dari pemkot.",
            "Kami butuh bantuan logistik secepatnya.",
            "Untung kasur saya mengapung."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang selalu datang ke rumahmu tepat di jam makan siang atau jam makan malam. Sindiran halus untuknya?",
        "pilihanJawaban": [
            "Kamu sengaja ya datang pas jam makan?",
            "Radar aroma masakan di hidungmu berfungsi dengan sangat baik ya.",
            "Kebetulan sekali, mari makan bersama.",
            "Lain kali datang jam 2 siang saja ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika sebuah tim sepak bola kalah telak 5-0, ucapan menghibur bernada sarkas dari pendukung lawan adalah?",
        "pilihanJawaban": [
            "Kalian mainnya jelek banget.",
            "Gak apa-apa kalah, yang penting kan dapet sehatnya.",
            "Kalian kurang beruntung saja hari ini.",
            "Besok latihan lagi yang rajin ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Seseorang mengeluh kamarnya berantakan seperti kapal pecah tapi malas membereskannya. Kalimat sarkas ibunya?",
        "pilihanJawaban": [
            "Bereskan kamarmu sekarang!",
            "Bagus, pertahankan terus estetikanya sampai kecoak bikin kerajaan di sini.",
            "Ibu cape melihat kamar kamu begini.",
            "Besok ibu panggilkan pembantu ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat pengendara motor yang masuk ke jalur Transjakarta lalu marah-marah saat ditilang polisi. Netizen menganggapnya?",
        "pilihanJawaban": [
            "Warga negara yang kritis",
            "Pemilik jalur khusus gaib",
            "Pahlawan jalan raya",
            "Korban salah paham"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu curhat galau nangis-nangis di medsos karena diputusin, padahal mereka baru pacaran selama 3 hari. Sarkas yang tepat?",
        "pilihanJawaban": [
            "Sabar ya, badai pasti berlalu.",
            "Dramanya luar biasa, mengalahkan rekor drakor 16 episode.",
            "Cepat amat putusnya, baru kemarin jadian.",
            "Cari yang baru lagi aja, gampang."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika ada orang kaya baru yang mendadak pura-pura sombong tidak kenal dengan teman-teman lamanya di kampung. Julukannya?",
        "pilihanJawaban": [
            "Orang sukses",
            "Kacang lupa kulitnya",
            "Manusia amnesia selektif",
            "Sultan dadakan"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Saat guru atau dosen memberikan tugas yang deadline-nya besok pagi jam 7 padahal baru dikasih jam 11 malam. Respons mahasiswa?",
        "pilihanJawaban": [
            "Tugas ini terlalu mendadak pak/bu.",
            "Terima kasih pak/bu, jadwal tidur malam memang terlalu over-rated bagi kami.",
            "Kami akan kerjakan sebisanya.",
            "Asyik, malam ini bisa begadang produktif."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Seorang politikus ketahuan tidur pulas saat sidang membahas nasib rakyat kecil. Sindiran netizen yang paling kena adalah?",
        "pilihanJawaban": [
            "Beliau sedang lelah bekerja demi rakyat.",
            "Tidur yang nyenyak ya pak, jangan sampai keganggu suara rakyat di luar.",
            "Kenapa rapatnya sambil tidur sih pak?",
            "Mungkin kursinya terlalu empuk."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu selalu meminjam barangmu (baju, sepatu, vape) tanpa pernah modal beli sendiri. Julukan yang cocok adalah?",
        "pilihanJawaban": [
            "Sahabat sejati",
            "Duta Saham Hak Milik Bersama",
            "Kolektor barang pinjaman",
            "Fasilitator gratisan"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat orang yang hobi komplain tentang polusi udara Jakarta yang buruk tapi ke minimarket depan kompleks sejauh 10 meter saja naik mobil. Kalimat sarkasnya?",
        "pilihanJawaban": [
            "Kamu berkontribusi pada polusi.",
            "Hebat, langkah kakimu sangat berharga sampai harus dilindungi mobil ya.",
            "Polusi udara memang semakin parah.",
            "Besok-besok jalan kaki aja biar sehat."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika pacarmu membalas pesan chat singkat cuma 'O' setelah kamu mengetik penjelasan sepanjang 5 paragraf. Arti dari 'O' tersebut adalah?",
        "pilihanJawaban": [
            "Dia sudah paham",
            "Sinyalnya lagi jelek",
            "Simulasi tanda berakhirnya dunia",
            "Dia lagi malas mengetik"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Ada orang yang mengkritik masakan restoran bintang lima bertarif mahal padahal dia dia sendiri masak mi instan saja sering kematangan. Sindirannya?",
        "pilihanJawaban": [
            "Lidahmu terlalu mewah untuk mi instan.",
            "Kritikus kuliner kelas dunia tingkat rukun tetangga.",
            "Masakan kamu sendiri belum tentu enak.",
            "Jangan sok tahu tentang makanan mahal."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat melihat drama settingan para artis di televisi demi menaikkan rating program mereka. Kalimat penonton yang cerdas?",
        "pilihanJawaban": [
            "Dramanya seru banget!",
            "Saking natural aktingnya, sampai-sampai naskahnya kelihatan di layar kaca.",
            "Saya tidak suka nonton acara TV lagi.",
            "Semoga mereka cepat baikan ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu membeli kamera mirrorless mahal seharga puluhan juta tapi hanya dipakai untuk foto mirror selfie di toilet. Sindiran yang tepat?",
        "pilihanJawaban": [
            "Kameranya bagus banget, hasilnya jernih.",
            "Spesifikasi dewa hanya untuk mengabadikan keindahan kloset ya.",
            "Sayang banget kameranya cuma buat foto di toilet.",
            "Bisa pinjam kameranya buat hunting foto?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika dipanggil ke ruang BK (Bimbingan Konseling) sekolah karena ketahuan bolos berjamaah. Jawaban kompak murid yang sarkas?",
        "pilihanJawaban": [
            "Kami minta maaf bu/pak.",
            "Kami cuma sedang melakukan studi banding ke warung sebelah, bu.",
            "Kami khilaf pak, jangan dihukum.",
            "Kemarin sekolahnya sepi jadi kami pulang."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada cowok yang mengaku setia setengah mati, tapi matanya otomatis melirik 180 derajat setiap ada cewek glowing lewat. Istilah sarkas untuknya?",
        "pilihanJawaban": [
            "Cowok setia bersyarat",
            "Spesialis pemantau radar kecantikan",
            "Lelaki buaya darat",
            "Pria berjiwa seni tinggi"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat seseorang yang dandanannya super tebal sampai warna wajah dan lehernya berbeda jauh. Sindiran netizen adalah?",
        "pilihanJawaban": [
            "Make-up kamu cantik sekali.",
            "Konsepnya bagus, wajahnya glow-up tapi lehernya masih mode dark-mode.",
            "Bedaknya ketebalan itu kak.",
            "Beli bedak merk apa sih?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat pengumuman nilai ujian keluar dan kamu mendapatkan nilai 20 dari 100. Kalimat apresiasi diri yang sarkas?",
        "pilihanJawaban": [
            "Saya bodoh sekali.",
            "Setidaknya saya berhasil menyelamatkan angka 0 dari kesepian.",
            "Duh, nilainya jelek banget, remedial nih.",
            "Soalnya susah banget, gak masuk akal."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika ditanya 'Kapan nikah?' oleh kerabat saat momen lebaran, jawaban sarkas terbaik untuk membungkam mereka adalah?",
        "pilihanJawaban": [
            "Nanti kalau gak sabtu ya minggu.",
            "Tunggu tenda cateringnya ibu yang bayar ya.",
            "Doakan saja secepatnya ya om/tante.",
            "Besok pagi kalau tidak kesiangan."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu hobi bikin story Instagram galau setiap jam seolah-olah dia manusia paling menderita sedunia. Sebutan yang pas?",
        "pilihanJawaban": [
            "Anak indie sejati",
            "Ketua Yayasan Penderitaan Abadi",
            "Manusia melankolis",
            "Si Paling Galau"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat anak kecil zaman sekarang yang umur 7 tahun sudah panggil 'Ayah-Bunda' ke pacarnya di medsos. Respons orang dewasa?",
        "pilihanJawaban": [
            "Anak zaman sekarang pacarannya ngeri.",
            "Wah, kecil-kecil sudah siap menanggung beban kartu keluarga ya.",
            "Orang tuanya ke mana sih kok gak diawasi?",
            "Lucu banget ya mereka pacaran."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika lampu mati dari pagi sampai malam, lalu customer service PLN merespons 'Mohon maaf atas ketidaknyamanannya'. Kalimat balasan warga?",
        "pilihanJawaban": [
            "Gak apa-apa, kami sangat menikmati sensasi hidup di zaman purba ini.",
            "Kapan lampunya menyala kembali?",
            "Tolong diperbaiki secepatnya ya.",
            "Lilin di rumah saya sampai habis nih."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Temanmu pinjam korek api (manter) saat nongkrong, lalu korek itu masuk ke kantong celananya secara otomatis. Pelaku ini disebut?",
        "pilihanJawaban": [
            "Pencuri korek",
            "Kolektor korek tidak sengaja",
            "Inspirator gerakan curanrek",
            "Sahabat kurang modal"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Seseorang pamit tidur jam 9 malam di chat, tapi akun game online-nya terdeteksi 'In-Game' sampai jam 3 subuh. Sindirannya?",
        "pilihanJawaban": [
            "Katanya tidur, kok malah main game?",
            "Wah, kamu kalau tidur matanya sambil nge-push rank ya?",
            "Hebat, tidurnya produktif sekali.",
            "Besok jangan bohong lagi ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika supir angkot ngetem nunggu penumpang selama 1 jam sampai lumutan. Kalimat protes penumpang yang halus tapi nusuk?",
        "pilihanJawaban": [
            "Bang, jalan sekarang dong, buru-buru nih.",
            "Bang, ini ngetemnya sampai saya punya anak cucu atau gimana?",
            "Supirnya malas banget sih ngetem terus.",
            "Turunin saya di sini aja deh bang."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang hobi pamer kutipan bijak tentang agama di statusnya, tapi perilakunya sehari-hari suka ghibahin tetangga. Julukannya?",
        "pilihanJawaban": [
            "Ustadz medsos",
            "Ahli surga jalur jalur prestasi",
            "Manusia dwi-fungsi (Religius-Ghibah)",
            "Kritikus moralitas"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Saat kamu memesan makanan via ojek online dan abangnya tersesat sampai ke kota sebelah. Ucapanmu saat dia sampai?",
        "pilihanJawaban": [
            "Kok lama banget sih pak?",
            "Wah, makasih pak sudah keliling pulau dulu sebelum anter makanan saya.",
            "Makanannya sudah dingin nih pak.",
            "Gak apa-apa pak, yang penting selamat."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat orang dewasa yang sepedaan di trotoar tempat pejalan kaki sambil bel-belin orang jalan kaki agar minggir. Sindiran yang pas?",
        "pilihanJawaban": [
            "Trotoar itu buat orang jalan kaki, bukan sepeda!",
            "Maaf bos, jalan rayanya kurang luas ya sampai trotoar dibeli juga?",
            "Supir sepedanya gak punya sopan santun.",
            "Minggir-minggir, rajanya mau lewat."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu mengeluh tugas sekolahnya susah banget, padahal dia sendiri belum membuka buku sama sekali dari awal semester. Dia adalah?",
        "pilihanJawaban": [
            "Siswa yang tertekan",
            "Pengamat kesulitan tanpa aksi",
            "Pakar malas berteori tinggi",
            "Korban kurikulum"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Ketika ada akun gosip menyebarkan berita hoaks demi menaikkan jumlah pengikut, reaksi netizen cerdas?",
        "pilihanJawaban": [
            "Wah, beritanya sangat informatif dan mendidik bangsa.",
            "Laporkan akun ini karena menyebar hoaks.",
            "Berita ini beneran atau bohong sih?",
            "Jangan percaya sama akun gosip."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Melihat orang yang bernyanyi di kamar mandi dengan suara fals sekelas sirine ambulans rusak. Komentar keluarganya?",
        "pilihanJawaban": [
            "Suaramu jelek banget, diam!",
            "Bakat menyanyimu sangat terpendam, sebaiknya dipendam selamanya saja.",
            "Tolong kecilkan suaramu, mengganggu tidur.",
            "Wah, suaramu unik ya, cocok jadi penyanyi."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat ada diskon besar-besaran di toko online tapi ongkos kirimnya ternyata 5 kali lipat dari harga barang. Istilahnya?",
        "pilihanJawaban": [
            "Diskon abal-abal",
            "Subsidi silang ke kantong kurir",
            "Keajaiban marketing modern",
            "Penipuan terselubung"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu selalu menolak diajak keluar dengan alasan 'sibuk banget kerja', padahal isi instastory-nya rebahan sambil nonton Netflix. Dia sibuk apa?",
        "pilihanJawaban": [
            "Sibuk membangun peradaban kasur",
            "Sibuk bekerja keras",
            "Sibuk mencari alasan baru",
            "Sibuk menghindari kamu"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Ketika nonton film bioskop lalu ada orang di belakangmu yang hobi menendang-nendang kursimu sepanjang film. Kalimat teguranmu?",
        "pilihanJawaban": [
            "Jangan tendang kursi saya dong!",
            "Mas/Mbak, kalau kakinya tremor hebat, mending ke dokter saraf dulu deh.",
            "Sopan sedikit ya kalau di bioskop.",
            "Biza diam tidak kakinya?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang pamer beli iPhone seri terbaru tapi makannya cuma mi instan dicampur nasi selama 3 bulan kedepan. Sindiran yang cocok?",
        "pilihanJawaban": [
            "Gaya sosialita, lambung menderita.",
            "Wah, iPhonenya keren banget, fiturnya lengkap.",
            "Demi gengsi rela merusak kesehatan ya.",
            "Besok beli iPad sekalian biar lengkap."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Saat upacara bendera di sekolah, cuaca sangat terik tapi pidato pembina upacara panjangnya mengalahkan novel Harry Potter. Batin para murid?",
        "pilihanJawaban": [
            "Pidatonya sangat memotivasi kami.",
            "Pak/Bu, singkat padat jelasnya bapak/ibu bikin dengkul kami mau copot.",
            "Kapan upacaranya selesai sih?",
            "Semoga pembina upacaranya cepat lelah."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu minta diajarkan materi matematika dari awal, tapi setiap kamu jelaskan matanya malah fokus main TikTok. Ucapan sarkasmu?",
        "pilihanJawaban": [
            "Perhatikan penjelasan saya dong!",
            "Materi di TikTok pasti lebih keluar di ujian besok ya.",
            "Kamu niat belajar atau tidak sih?",
            "Nanti kalau tidak paham jangan salahkan saya ya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika ada orang yang mengendarai mobil mewah tapi membuang puntung rokok menyala dari jendela ke jalan raya. Sebutan paling pas?",
        "pilihanJawaban": [
            "Orang kaya berkelas",
            "Orang kaya berdompet tebal berotak hampa",
            "Pengendara arogan",
            "Sultan kurang edukasi"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat kamu bertanya arah jalan ke warga sekitar dan mereka menjawab 'Lurus aja mas dekat kok', tapi ternyata jaraknya 10 kilometer lagi. Arti kata 'dekat' adalah?",
        "pilihanJawaban": [
            "Kurang dari 500 meter",
            "Jarak pandang mata elang",
            "Dekat kalau naik jet pribadi",
            "Simulasi jalan sehat lintas provinsi"
        ],
        "indeksJawabanBenar": 3
    },
    {
        "teksPertanyaan": "Melihat seseorang yang mengaku depresi berat karena tidak sengaja menghilangkan skin kosmetik game online-nya. Komentar sarkas netizen?",
        "pilihanJawaban": [
            "Beban hidupmu sangat berat ya dek, mengalahkan krisis global.",
            "Sabar ya, semoga dapet ganti yang lebih bagus.",
            "Lebay banget sih, cuma game doang.",
            "Sini akunmu aku belikan skin baru."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Ketika ada seseorang yang hobi pamer pencapaian kerja keras orang lain (orang tua atau saudaranya) seolah itu miliknya sendiri. Dia dijuluki?",
        "pilihanJawaban": [
            "Anak berbakti",
            "Manusia numpang ketenaran keluarga",
            "Manager investasi kehormatan keluarga",
            "Pewaris takhta khayalan"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Temanmu bilang 'Aku gak belajar sama sekali semalam' sebelum ujian, tapi pas nilainya keluar dia dapet nilai 100 sendiri. Dia adalah?",
        "pilihanJawaban": [
            "Orang jenius",
            "Manusia fiktif bermuka dua",
            "Impostor berkedok merendah",
            "Siswa beruntung"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Saat ada berita kriminal tentang pelaku begal berdarah dingin, tapi netizen di kolom komentar malah fokus memuji wajah pelaku yang 'ganteng'. Fenomena ini disebut?",
        "pilihanJawaban": [
            "Keadilan sosial bagi seluruh rakyat Indonesia",
            "Krisis moralitas akut jalur visual",
            "Dukungan moral tanpa batas",
            "Apresiasi seni wajah kriminal"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu sedang buru-buru ke kamar mandi umum karena sudah di ujung tanda tanya, tapi orang di dalamnya malah asyik bernyanyi 5 lagu berturut-turut. Respons gedoran pintumu?",
        "pilihanJawaban": [
            "Woi cepat keluar, saya kebelet!",
            "Mas, konser tunggalnya bisa dilanjut di studio musik aja gak?",
            "Tolong hargai orang yang mengantre.",
            "Bisa dipercepat tidak urusannya?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika sebuah game online merilis update patch baru seukuran 50GB tapi isinya cuma memperbaiki bug visual rumput. Komentar para gamer?",
        "pilihanJawaban": [
            "Developer game ini sangat rajin.",
            "Gila, storage habis demi tekstur rumput yang lebih estetik.",
            "Patch ini tidak berguna sama sekali.",
            "Saya hapus saja game ini."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang mengkritik hasil foto fotografer profesional jelek, padahal dia sendiri memotret objek selalu blur dan miring. Istilahnya?",
        "pilihanJawaban": [
            "Kritikus handal",
            "Pakar fotografi abstrak tanpa kamera",
            "Orang sirik",
            "Kolektor foto gagal"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat kamu membeli baju secara online, pas datang ukurannya sangat kecil cukup untuk boneka barbie saja. Komentar ulasan bintang 1 kamu?",
        "pilihanJawaban": [
            "Bajunya kekecilan, saya kecewa.",
            "Sangat puas, baju ini cocok sekali untuk kucing peliharaan saya yang baru lahir.",
            "Toko ini penipu, jangan beli di sini.",
            "Bisa ditukar dengan ukuran yang lebih besar?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu curhat kalau pacarnya selingkuh untuk yang ke-18 kalinya tapi dia tetap mau memaafkan karena 'dia bisa berubah'. Sebutan yang pas buat temanmu?",
        "pilihanJawaban": [
            "Orang yang pemaaf",
            "Calon peraih penghargaan malaikat pelindung sedunia",
            "Bucin idiot level maksimal",
            "Sahabat setia"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat segerombolan orang yang nongkrong di kafe mahal berjam-jam tapi cuma memesan satu gelas es teh manis botolan dibagi bertiga. Sarkas pemilik kafe?",
        "pilihanJawaban": [
            "Terima kasih sudah meramaikan kafe kami sampai modal sewa ruko kami terancam.",
            "Kalian pelit sekali, pesan makanan dong!",
            "Silakan nongkrong sepuasnya ya kak.",
            "Besok-besok pesan satu-satu ya minumnya."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Ketika ada seseorang yang hobi melanggar rambu lalu lintas lalu saat ditilang dia mengeluarkan jurus 'Saya itu saudaranya Jenderal X'. Respons polisi yang bosan?",
        "pilihanJawaban": [
            "Oh maaf pak, silakan jalan terus.",
            "Wah, selamat ya, salam balik buat jenderal khayalan bapak.",
            "Tunjukkan surat-surat kendaraan bapak sekarang.",
            "Jangan bawa-bawa nama pejabat di sini."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat kamu presentasi kerja kelompok lalu temanmu memberikan pertanyaan super sulit yang menjatuhkanmu di depan kelas. Dia sejenis teman yang?",
        "pilihanJawaban": [
            "Kritis dan cerdas",
            "Musuh dalam selimut berkedok sahabat nabi",
            "Suka mencari perhatian guru",
            "Kurang paham materi"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang hobi mengeluh di media sosial kalau dia kesepian jomblo bertahun-tahun, tapi setiap ada yang ngedeketin langsung di-ghosting. Karakter ini disebut?",
        "pilihanJawaban": [
            "Pemilih dalam mencari pasangan",
            "Kolektor drama kesepian mandiri",
            "Jomblo sejati",
            "Manusia trauma masa lalu"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika kuota internetmu habis tepat di saat kamu sedang berada di pertengahan duel sengit game rank. Kalimat pujian sarkas untuk provider?",
        "pilihanJawaban": [
            "Provider ini payah banget.",
            "Luar biasa timingnya, sinyal hilang tepat di momen penentuan nasib bintang saya.",
            "Saya benci provider ini.",
            "Besok saya beli kartu perdana baru."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat tulisan 'Dilarang Parkir' di depan toko, tapi tepat di bawah papan itu berjejer 10 motor terparkir rapi. Fungsi papan larangan itu adalah?",
        "pilihanJawaban": [
            "Penanda tempat parkir khusus",
            "Hiasan estetik tata ruang kota",
            "Aturan resmi pemerintah",
            "Tempat berteduh burung liar"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu berkata 'Aku otw (on the way)' saat janjian, padahal dia baru saja bangun tidur dan masih pakai sarung di kasur. Singkatan 'otw' bagi dia berarti?",
        "pilihanJawaban": [
            "On the way (Sedang di jalan)",
            "Ok tunggunya woy (Masih mager)",
            "Otw ngumpulin nyawa dulu",
            "Orang tanpa wujud"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Ketika ada orang yang mengaku ahli investasi saham kelas internasional tapi uang tabungannya sendiri habis dipakai main judi slot. Julukan netizen?",
        "pilihanJawaban": [
            "Pakar finansial",
            "Inspirator investasi masa depan",
            "Spesialis sedekah paksa ke bandar luar negeri",
            "Korban ekonomi digital"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Melihat film horor Indonesia yang isinya lebih banyak memamerkan adegan jumpscare suara jedag-jedug keras daripada plot cerita yang jelas. Ulasan penonton?",
        "pilihanJawaban": [
            "Filmnya seru dan menakutkan.",
            "Cocok untuk membersihkan kotoran telinga karena sound systemnya menggelegar.",
            "Alur ceritanya kurang menarik.",
            "Hantu di film ini sangat menyeramkan."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang kerjaannya pamer sertifikat seminar puluhan lembar di LinkedIn tapi saat disuruh kerja nyata kebingungan setengah mati. Dia mengidap sindrom?",
        "pilihanJawaban": [
            "Kolektor kertas gelar akademik",
            "Spesialis pemburu takhta portofolio gaib",
            "Karyawan teladan",
            "Terlalu banyak belajar"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat kamu curhat masalah berat ke temanmu, dan dia merespons dengan 'Ah kamu mending, lah aku...', tindakan temanmu disebut?",
        "pilihanJawaban": [
            "Memberikan solusi alternatif",
            "Ajang kompetisi penderitaan internasional",
            "Menghibur sahabat yang sedih",
            "Kurang peka empati"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika harga tiket pesawat domestik lebih mahal daripada tiket penerbangan ke luar negeri. Komentar sarkas pelancong?",
        "pilihanJawaban": [
            "Mari kita cintai produk lokal dengan berwisata ke luar negeri saja.",
            "Harga tiket pesawat dalam negeri tidak masuk akal.",
            "Pemerintah tolong turunkan harga tiket domestik.",
            "Lebih baik naik kereta saja kalau begitu."
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Melihat instruktur senam yang badannya gemuk bugar menyuruh ibu-ibu diet ketat makan sayur setiap hari. Kalimat batin peserta senam?",
        "pilihanJawaban": [
            "Ibu instrukturnya sangat bersemangat.",
            "Teorinya bagus bu, besok-besok kita praktek bareng di tukang bakso ya.",
            "Senam hari ini sangat menguras tenaga.",
            "Saya harus ikuti saran diet dari instruktur."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu berjanji menjaga rahasia berdua saja, tapi 5 menit kemudian seluruh satu angkatan sekolah sudah tahu ceritanya. Rahasia berdua artinya?",
        "pilihanJawaban": [
            "Rahasia privat",
            "Berdua dengan seluruh isi kontak WhatsApp dia",
            "Cerita seru untuk digosipkan",
            "Informasi umum tanpa batas"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika kamu membeli mi ayam seharga Rp5.000 dan potongan daging ayamnya sekecil debu kosmik hingga tidak terlihat mata telanjang. Kalimat pujianmu ke penjual?",
        "pilihanJawaban": [
            "Mi ayamnya kurang banyak dagingnya mang.",
            "Luar biasa mang, teknik memotong ayamnya tipis sekelas molekul atom nuklir.",
            "Rasanya enak tapi porsinya sedikit.",
            "Besok-besok potongan dagingnya diganti yang besar ya mang."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang mengaku tidak suka gosip, tapi matanya berbinar-binar cerah saat mendengar kata 'Eh kamu tahu si X gak?'. Karakter ini dinamakan?",
        "pilihanJawaban": [
            "Manusia anti-sosial",
            "Intelektual penyaring berita lingkungan",
            "Menteri penerangan info valid tetangga",
            "Duta ghibah berkedok jurnalisme warga"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Saat seseorang mengunggah video komedi buatan sendiri tapi garingnya mengalahkan kerupuk warung kaleng 3 hari dibuka. Komentar netizen?",
        "pilihanJawaban": [
            "Videonya lucu sekali menghibur.",
            "Saking lucunya, saya sampai lupa cara tertawa yang benar gimana.",
            "Besok-besok jangan bikin video komedi lagi.",
            "Bakat komedimu perlu diasah kembali."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika sistem aplikasi pendaftaran online milik pemerintah mendadak 'Server Error' tepat di hari pertama pembukaan pendaftaran jam 00.01. Respons pendaftar?",
        "pilihanJawaban": [
            "Servernya kurang kapasitas nih.",
            "Sangat konsisten dengan tradisi infrastruktur IT digital negara kita tercinta.",
            "Tolong perbaiki servernya admin.",
            "Mungkin pendaftarnya terlalu banyak."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Seseorang mengendarai mobil mewah keluaran terbaru tapi enggan membayar tarif tol Rp5.000 dan malah memaksa nempel mobil depan agar gratis. Dia menderita?",
        "pilihanJawaban": [
            "Kemiskinan mentalitas akut berbalut casing kaya",
            "Kurang saldo kartu e-toll",
            "Sifat hemat yang luar biasa",
            "Krisis keuangan mendadak"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Temanmu curhat kalau dia lelah bekerja bagai kuda demi masa depan, padahal kesehariannya adalah magang tanpa digaji di perusahaan saudaranya sendiri. Status dia adalah?",
        "pilihanJawaban": [
            "Pekerja keras sejati",
            "Pahlawan investasi tenaga sukarela keluarga",
            "Korban eksploitasi kekerabatan",
            "Karyawan magang mandiri"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat spanduk kampanye caleg yang fotonya diedit super mulus tanpa pori-pori mengalahkan kulit bayi korea. Komentar warga?",
        "pilihanJawaban": [
            "Calegnya ganteng/cantik banget.",
            "Semoga visi misinya semulus proses editing wajah bapak/ibu di spanduk ya.",
            "Fotonya terlalu banyak editan itu.",
            "Bisa minta nomor kontak editor fotonya?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu meminjamkan buku catatan rapi ke temanmu, pas dikembalikan bukunya penuh coretan abstrak dan noda kuah bakso. Ucapan terima kasihmu?",
        "pilihanJawaban": [
            "Kenapa buku saya kotor sekali?",
            "Kreatif banget, buku catatan saya sekarang dapet dekorasi seni kontemporer kuah kaldu.",
            "Besok jangan pinjam buku saya lagi.",
            "Makasih ya udah dibalikin bukunya."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang hobi mengkritik sistem pendidikan Indonesia hancur, padahal dia sendiri sering bolos sekolah demi main game di rental PS. Dia pantas disebut?",
        "pilihanJawaban": [
            "Pengamat pendidikan kritis",
            "Aktivis reformasi pelajar jalur rental",
            "Siswa nakal berwawasan luas",
            "Korban kegagalan kurikulum merdeka"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Saat melihat acara talkshow televisi yang isinya cuma mengadu domba dua kubu demi menaikkan engagement media sosial. Komentar penonton cerdas?",
        "pilihanJawaban": [
            "Acaranya seru banget menegangkan.",
            "Sangat edukatif, tontonan wajib untuk mencerdaskan kehidupan bangsa kita.",
            "Acara ini tidak bermutu sama sekali.",
            "Semoga produser acaranya dapet hidayah."
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu mengeluh tidak punya baju untuk dipakai ke pesta nongkrong malam ini, padahal isi lemarinya tumpah keluar saking banyaknya. Kondisi ini dinamakan?",
        "pilihanJawaban": [
            "Kekurangan sandang akut khayalan wanita",
            "Lemarinya kekecilan ukuran",
            "Butuh belanja baju baru lagi",
            "Sindrom amnesia isi pakaian"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Ketika ada seseorang yang hobi pamer mengonsumsi vitamin mahal pelindung tubuh, tapi merokok habis 3 bungkus per hari. Sistem imun tubuhnya berstatus?",
        "pilihanJawaban": [
            "Sangat sehat dan kuat",
            "Simulasi perang dunia ketiga di dalam paru-paru",
            "Kekurangan asupan gizi seimbang",
            "Dilindungi suplemen pelindung"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat pengendara mobil yang menggunakan sirine patwal ilegal menyuruh semua kendaraan minggir demi melintasi jalanan macet. Istilah sarkasnya?",
        "pilihanJawaban": [
            "Presiden dadakan lintas jalur lambat",
            "Pengendara darurat ambulans siluman",
            "Orang kaya buru-buru urusan negara",
            "Sultan pemilik aspal jalan raya"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Kamu membeli barang elektronik murah meriah seharga Rp10.000, pas dinyalakan langsung meledak mengeluarkan asap hitam. Kalimat ulasanmu?",
        "pilihanJawaban": [
            "Barangnya rusak bahaya banget.",
            "Luar biasa efek fiturnya, merangkap jadi kembang api mini perayaan tahun baru.",
            "Jangan beli barang murah di toko ini.",
            "Bisa klaim garansi produk tidak ya?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada teman yang selalu datang paling awal saat pembagian makanan gratis, tapi mendadak hilang gaib saat diajak iuran bayar kosan bersama. Julukannya?",
        "pilihanJawaban": [
            "Sahabat sejati pemburu logistik gratis",
            "Aktivis sosial penikmat subsidi kuliner",
            "Spesialis pencari berkah makan malam",
            "Manusia amnesia finansial situasional"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat rumah mewah berlantai 3 dengan mobil sport berjejer di garasi, tapi di depan pagarnya tertempel stiker 'Keluarga Miskin Penerima Bantuan Bansos'. Warga menilai?",
        "pilihanJawaban": [
            "Pemiliknya orang kaya yang rendah hati",
            "Keajaiban verifikasi data aparatur desa setempat",
            "Bantuan bansosnya salah sasaran",
            "Keluarganya sedang mengalami penurunan ekonomi"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu pamer kalau dia baru saja membeli laptop gaming spesifikasi tertinggi Core i9 RTX 4090, tapi penggunaan hariannya cuma untuk mengetik Ms Word. Laptop tersebut berfungsi sebagai?",
        "pilihanJawaban": [
            "Mesin ketik termahal abad ke-21",
            "Investasi teknologi masa depan",
            "Laptop penunjang karir admin",
            "Alat pamer gengsi mahasiswa"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Saat kamu mendengarkan lagu galau kesukaanmu di YouTube, tapi di tengah-tengah lagu muncul iklan judi online jedag-jedug keras. Nuansa estetik lagumu berubah menjadi?",
        "pilihanJawaban": [
            "Semakin sedih merenung nasib",
            "Konser dangdut keliling jalur judi internasional",
            "Terganggu iklan tidak jelas",
            "Lagu galaunya jadi lebih asyik"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang hobi mengomentari cara asuh anak artis di media sosial salah total, padahal dia sendiri belum menikah dan pelihara kucing saja sering kabur. Sebutannya?",
        "pilihanJawaban": [
            "Pakar ilmu parenting khayalan publik",
            "Kritikus sosial kehidupan keluarga artis",
            "Netizen peduli anak bangsa",
            "Konsultan psikologi anak dadakan"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Ketika melihat proses pembuatan jalan aspal baru di kompleks perumahan yang ketebalannya setipis kulit bawang kating. Umur ketahanan jalan tersebut diperkirakan?",
        "pilihanJawaban": [
            "Bisa bertahan sampai 10 tahun",
            "Hancur seketika saat dilindas gerobak siomay mang maman",
            "Kualitas aspalnya kurang bagus",
            "Perlu dilapisi semen tambahan"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu meminjamkan akun premium aplikasi streaming film ke sahabatmu, besoknya password akun tersebut diganti tanpa sepengetahuanmu. Sahabatmu berjiwa?",
        "pilihanJawaban": [
            "Pencuri akun profesional",
            "Inspirator gerakan nasional hak milik sepihak",
            "Kurang sopan santun berteman",
            "Pencinta film gratisan akut"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada siswa yang rajin sekali membuat rangkuman materi pelajaran pakai 10 warna pulpen estetik berbeda, tapi pas ujian nilainya tetep merah merona. Kompetensi dia adalah?",
        "pilihanJawaban": [
            "Siswa berbakat seni kaligrafi catatan",
            "Anak rajin kurang beruntung ujian",
            "Spesialis dekorasi buku tulis nasional",
            "Kurang memahami kisi-kisi soal"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Ketika kamu memesan es teh manis di warung makan, es batunya penuh menumpuk sampai ke ujung gelas sementara air tehnya cuma 3 sendok makan. Menu tersebut sejatinya adalah?",
        "pilihanJawaban": [
            "Minuman segar pelepas dahaga",
            "Simulasi bongkahan es kutub utara mencair dini",
            "Es teh kurang air",
            "Menu hemat es batu"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat video tutorial cara menjadi kaya raya dalam 5 menit modal rebahan buatan influencer yang aslinya dapet kekayaan dari warisan kakeknya. Video itu bergenre?",
        "pilihanJawaban": [
            "Edukasi finansial bisnis",
            "Komedi fiksi ilmiah bermotif motivasi",
            "Tutorial sukses nyata",
            "Tips investasi aman"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu mengaku fans berat band rock alternatif legendaris dari Amerika, tapi pas ditanya judul lagu selain yang viral di TikTok langsung kebingungan. Dia fans jalur?",
        "pilihanJawaban": [
            "Fans sejati garis keras",
            "Fans jalur algoritma fyp fiktif populis",
            "Pencinta musik kasual",
            "Baru menyukai band tersebut"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika ada aturan dilarang membawa makanan dari luar ke dalam area bioskop, respons penonton emak-emak kreatif adalah?",
        "pilihanJawaban": [
            "Mematuhi aturan dengan tertib",
            "Teknik kamuflase nasi bungkus di dalam tas mukena",
            "Membeli makanan mahal di dalam bioskop",
            "Memprotes kebijakan manajemen bioskop"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu sedang asyik bermain game FPS kompetitif, lalu anggota timmu berjalan maju lurus ke arah musuh tanpa menembak seperti bot rusak. Kontribusi dia untuk tim?",
        "pilihanJawaban": [
            "Membantu umpan deteksi posisi musuh",
            "Duta donatur poin cuma-cuma ke kubu lawan",
            "Pemain pemula kurang latihan",
            "Mengalami kendala koneksi lag"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang kerjaannya pamer saldo rekening bank puluhan juta di medsos hasil editan inspect element Google Chrome. Istilah profesi gaibnya?",
        "pilihanJawaban": [
            "Sultan digital fiktif",
            "Pakar coding manipulasi finansial",
            "Crazy rich jalur inspect element",
            "Pengusaha sukses internet"
        ],
        "indeksJawabanBenar": 2
    },
    {
        "teksPertanyaan": "Melihat berita tentang proyek jembatan desa berbiaya Rp5 miliar rupiah yang baru diresmikan kemarin sore, tapi ambruk tadi subuh karena tertiup angin kencang. Faktor utamanya?",
        "pilihanJawaban": [
            "Bencana alam cuaca ekstrem",
            "Kualitas semen berbahan dasar tepung terigu cap segitiga biru",
            "Kesalahan teknis kalkulasi arsitek",
            "Kurang doa selamat saat peresmian"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Teman kamu kelompoki pmit ijin tidak ikut kerja kelompok karena mau fokus 'beribadah menenangkan diri', pas dicek ternyata lagi asyik mabar kencan di game online. Dia mengamalkan konsep?",
        "pilihanJawaban": [
            "Ibadah penenang jiwa raga",
            "Spesialis dusta religius situasional",
            "Keseimbangan dunia akhirat khayalan",
            "Pelajar kurang disiplin tugas"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat antrean pembagian sembako gratis yang panjangnya mencapai 2 kilometer, sementara panitianya baru datang jam 4 sore bawa 10 kotak mie instan. Rasio ketersediaannya?",
        "pilihanJawaban": [
            "Sangat cukup memadai warga",
            "Simulasi ketahanan pangan tingkat dewa bencana",
            "Panitianya kurang koordinasi logistik",
            "Sembakonya habis dibagikan awal"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada cowok yang hobi mengomentari cewek lain kurang glowing modis di medsos, padahal dia sendiri mandi cuma sekali sehari kalau ingat. Cowok ini berstandar?",
        "pilihanJawaban": [
            "Pencinta keindahan visual tinggi",
            "Kritikus kecantikan tanpa modal mandi wajib",
            "Lelaki idaman masa kini",
            "Kurang menjaga kebersihan diri"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu membeli casing hp bergambar estetik keren di toko online, pas datang gambarnya buram pecah-pecah sekelas resolusi video 3gp tahun 2005. Kalimat ulasanmu?",
        "pilihanJawaban": [
            "Casing hp nya jelek banget parah.",
            "Sangat bernuansa retro klasik purba, melatih mata saya mendeteksi pixel rusak.",
            "Jangan beli aksesoris hp di toko ini.",
            "Bisa ajukan retur barang rusak adm?"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat instruktur gym berotot kekar menyuruh anggotanya konsisten angkat beban berat tiap subuh, tapi dia sendiri ke gym diantar supir pribadi karena malas menyetir. Istilahnya?",
        "pilihanJawaban": [
            "Motivator kebugaran fisik mandiri",
            "Inspirator angkat beban jalur komando supir",
            "Pelatih gym kurang disiplin waktu",
            "Binaragawan profesional berkelas"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu meminjam akun wifi id premium milikmu untuk urusan 'kerjain tugas sekolah penting', pas dicek kuotanya habis 100GB dipakai download semua episode anime. Tugas sekolahnya bertema?",
        "pilihanJawaban": [
            "Studi literatur budaya pop jepang modern",
            "Tugas akhir analisis animasi digital",
            "Urusan mendesak siswa teladan",
            "Tugas fiktif pemburu kuota sahabat"
        ],
        "indeksJawabanBenar": 0
    },
    {
        "teksPertanyaan": "Ketika ada diskon flash sale barang elektronik seharga Rp99 perak, tapi pas kamu klik di detik ke-0.0001 langsung muncul tulisan 'Stok Habis'. Pelaku borongnya adalah?",
        "pilihanJawaban": [
            "Pembeli tercepat di dunia",
            "Pasukan bot siluman peliharaan server marketplace",
            "Sistem websitenya lagi eror bug",
            "Konsumen beruntung tingkat nasional"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang hobi pamer foto liburan mewah di menara eiffel paris hasil editan photoshop kasar sampai menaranya condong ke kanan. Lokasi liburan aslinya?",
        "pilihanJawaban": [
            "Eropa barat sekitar prancis",
            "Studio rental komputer edit foto pojok kampung",
            "Destinasi wisata lokal berkelas",
            "Tempat liburan khayalan selebgram"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat sinetron televisi Indonesia yang adegan kecelakaannya ditabrak gerobak sampah tapi korbannya amnesia permanen sampai lupa nama sendiri. Kualitas skenarionya?",
        "pilihanJawaban": [
            "Sangat dramatis menyentuh hati penonton",
            "Mahakarya fiksi medis tingkat rukun warga",
            "Alur ceritanya kurang masuk akal kesehatan",
            "Sinetron favorit ibu-ibu kompleks sekitar"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu curhat kalau dia patah hati berat ditinggal nikah pacarnya, padahal hubungan mereka cuma status komitmen virtual tanpa pernah ketemu fisik. Istilah hubungannya?",
        "pilihanJawaban": [
            "Kisah cinta tragis romantis dunia digital",
            "Simulasi pacaran fiktif bermodal kuota internet",
            "Hubungan jarak jauh ldr sejati",
            "Pacaran modern generasi alpha"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat spanduk warung bakso bertuliskan 'Bakso Daging Sapi Asli Tanpa Campuran Boraks', tapi tekstur baksonya kenyal membal bisa dipakai main pingpong. Kandungan utamanya?",
        "pilihanJawaban": [
            "Daging sapi segar pilihan",
            "Karet ban dalam motor merk fdr campur tepung kanji",
            "Resep rahasia kuliner nusantara",
            "Bahan pengawet aman konsumsi"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu meminjamkan powerbank kapasitas besar ke temanmu pas nongkrong, pas dibalikin dayanya kosong total dan kabelnya putus dalam. Sifat temanmu?",
        "pilihanJawaban": [
            "Kurang hati-hati pinjam barang elektronik",
            "Spesialis penghisap daya baterai tanpa sisa modal pertemanan",
            "Sahabat dekat kurang modal nongkrong",
            "Karyawan magang pemburu charger gratis"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada tetangga yang hobi komplain suara musik rumahmu berisik, padahal dia sendiri kalau karaokean tiap sabtu malam suaranya menggelegar pakai speaker hajatan ruko. Dia mengidap?",
        "pilihanJawaban": [
            "Sensitivitas pendengaran telinga akut",
            "Sindrom egois musikalitas ganda rukun tetangga",
            "Kurang menyukai genre musik rumahmu",
            "Gangguan ketenangan lingkungan sekitar"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat papan rambu jalan tol tertulis 'Kecepatan Minimal 60 km/jam', tapi kondisi aspal di depan macet total macet cet tidak bergerak sepanjang 5 kilometer. Kecepatannya?",
        "pilihanJawaban": [
            "Sesuai standar aturan pengelola jalan tol",
            "Simulasi parkir massal lintas kendaraan nasional",
            "Mengalami kendala volume arus mudik",
            "Kecepatan berkendara kurang stabil"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu membeli kemeja putih formal untuk magang kerja di toko grosir online, pas datang kemejanya transparan menerawang tembus pandang sekelas kain kelambu nyamuk. Fungsinya?",
        "pilihanJawaban": [
            "Baju formal kerja kantoran magang",
            "Casing pakaian luar detektor masuk angin dini",
            "Fashion item modern tren anak muda",
            "Baju santai rumahan musim panas"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat video motivasi 'Cara sukses jadi milyarder umur 20 tahun tanpa modal' buatan pemuda yang aslinya dapet modal bisnis dari investasi dana tanpa batas orang tuanya. Kategori videonya?",
        "pilihanJawaban": [
            "Inspirasi bisnis UMKM anak muda",
            "Dongeng pengantar tidur bermotif kapitalis visual",
            "Tutorial wirausaha mandiri sukses nyata",
            "Tips sukses finansial generasi z"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu mengaku ahli gizi kebugaran tubuh karena sering baca thread di Twitter, tapi dia sendiri sarapan pagi pakai mi instan double dicampur nasi putih plus kerupuk. Status keahliannya?",
        "pilihanJawaban": [
            "Konsultan nutrisi kasual media sosial",
            "Pakar karbohidrat tingkat tinggi rukun tetangga",
            "Siswa peduli pola makan sehat",
            "Korban misinformasi kesehatan internet"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat logo instansi pelayanan publik bertuliskan 'Melayani dengan Sepenuh Hati', tapi petugas loketnya cemberut ketus judes mengalahkan singa kelaparan. Konsep pelayanannya?",
        "pilihanJawaban": [
            "Ramah tamah profesional standar nasional",
            "Simulasi uji kesabaran iman tingkat tinggi pendaftar warga",
            "Petugas loketnya sedang lelah bekerja",
            "Sistem pelayanan kurang maksimal administrasi"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu sedang asyik menonton video tutorial coding di YouTube serius, tiba-tiba muncul iklan motivator berteriak 'Kamu masih miskin karena malas!'. Respons spontan batinmu?",
        "pilihanJawaban": [
            "Sangat termotivasi bekerja keras lagi",
            "Terima kasih diingatkan bos jualan kelas premiumnya skip aja",
            "Terganggu fokus belajar pemrograman coding",
            "Motivatornya sangat bersemangat menginspirasi"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang hobi memamerkan foto buku tebal bertema filsafat eksistensialisme di status medsosnya, tapi aslinya halaman buku itu belum pernah dibuka dari segel plastik. Dia kolektor?",
        "pilihanJawaban": [
            "Pencinta literatur buku filsafat klasik",
            "Pakar pamer intelektualitas jalur segel plastik",
            "Mahasiswa rajin pemburu buku langka",
            "Kolektor buku bacaan harian rumah"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat proses renovasi trotoar kota yang dibongkar pasang tiap akhir tahun menjelang anggaran habis, padahal kondisi trotoarnya masih mulus bagus tanpa cacat. Proyek ini dinamakan?",
        "pilihanJawaban": [
            "Perawatan infrastruktur rutin tata kota",
            "Gerakan nasional penghabisan sisa dana anggaran akhir tahun",
            "Peningkatan fasilitas kenyamanan pejalan kaki",
            "Perbaikan mutu fasilitas umum daerah"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu ijin ke toilet pamit pas giliran urutan dia bayar tagihan makan bersama di kafe nongkrong, lalu nongol lagi pas nota bill-nya udah lunas dibayar temen lain. Jurus gaib ini bernama?",
        "pilihanJawaban": [
            "Teknik kabur darurat urusan pencernaan",
            "Strategi kamuflase finansial hemat dompet pertemanan",
            "Sifat lupa bayar kasual siswa nongkrong",
            "Kendala medis mendadak jam makan malam"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat pengumuman lowongan kerja tertulis 'Mencari Karyawan Berjiwa Loyalitas Tinggi Tanpa Batas Waktu', itu adalah kode rahasia perusahaan untuk?",
        "pilihanJawaban": [
            "Lingkungan kerja profesional dan disiplin",
            "Simulasi kerja rodi lembur gratisan tanpa uang bonus",
            "Perusahaan pencari bakat muda berpotensi",
            "Sistem kerja fleksibel mengutamakan performa"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada teman yang hobinya pasang status WhatsApp bijak tentang indahnya berbagi ikhlas sedekah tiap pagi, tapi ditagih iuran kas kelas Rp5.000 susahnya minta ampun. Karakter dia?",
        "pilihanJawaban": [
            "Siswa religius penenang suasana kelas",
            "Manusia dwi-fungsi berteori tinggi pelit realita",
            "Anak kurang mampu bayar iuran kas",
            "Pengingat kebaikan moral harian sekolah"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu membeli earphone bluetooth super murah seharga Rp5.000 di pasar maling, pas dicoba suaranya kresek-kresek sekelas frekuensi radio komunikasi kapal selam karam. Kualitas audionya?",
        "pilihanJawaban": [
            "Audio standar kasual pendengar musik",
            "Simulasi efek suara perang dunia pertama sektor parit pertahanan",
            "Earphone hp rusak cacat produksi pabrik",
            "Kurang cocok dengan bass lagu modern"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat influencer kecantikan mengunggah video tutorial skin care wajah glowing natural alami, tapi di balik layarnya pakai filter kecantikan level maksimal 100%. Rahasia glowingnya adalah?",
        "pilihanJawaban": [
            "Asupan vitamin kulit bergizi pilihan",
            "Keajaiban algoritma pemrosesan filter gpu smartphone canggih",
            "Produk kosmetik kecantikan merk ternama internasional",
            "Perawatan dokter ahli kecantikan wajah berkala"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu mengaku gamers hardcore tingkat turnamen internasional e-sports, tapi pas diajak main game rank bareng dapet skor eliminasi 0 mati 15 kali berturut-turut. Kompetensi dia adalah?",
        "pilihanJawaban": [
            "Gamer berpengalaman strategi bertahan lama",
            "Donatur poin rank cuma-cuma pelindung bintang kubu lawan",
            "Pemain kasual penikmat game online sore",
            "Mengalami kendala teknis jaringan internet rumah"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat berita tentang pejabat daerah yang menggelar rapat koordinasi penanggulangan kemiskinan warga di dalam gedung hotel bintang lima mewah berbintang emas. Konsep rapatnya?",
        "pilihanJawaban": [
            "Evaluasi kinerja penanganan krisis sosial daerah",
            "Simulasi kemewahan di tengah penderitaan rakyat kecil",
            "Rapat dinas resmi aparatur sipil negara",
            "Koordinasi penting instansi terkait penanganan bencana"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu memesan menu sate kambing di warung pinggir jalan, pas digigit dagingnya keras alot mengalahkan ketahanan karet ban mobil fuso muatan batubara. Kualitas daging kambingnya?",
        "pilihanJawaban": [
            "Daging kambing muda pilihan penuh gizi",
            "Daging kambing purba berotot baja pelatih kekuatan gigi geraham",
            "Cara memasak daging kambing kurang matang sempurna",
            "Porsi hemat daging sate kambing pinggir jalan"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang kerjaannya komentar mengkritik karya desain grafis desainer profesional hancur total, padahal dia sendiri bikin poster pakai aplikasi canva template bawaan langsung ganti teks. Profesinya?",
        "pilihanJawaban": [
            "Kritikus seni visual modern kompeten",
            "Pakar desain grafis jalur instan template bawaan canva",
            "Netizen peduli estetika karya seni digital",
            "Desainer pemula minim edukasi seni grafis"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat pameran seni kontemporer internasional yang isinya cuma memajang satu buah pisang matang dilakban hitam di dinding gedung, lalu terjual seharga Rp2 miliar rupiah. Nilai seninya terletak pada?",
        "pilihanJawaban": [
            "Makna filosofis mendalam tentang kehidupan manusia modern",
            "Tingkat kelucuan transaksi keuangan kolektor kaya raya kurang hiburan",
            "Keunikan karya seni rupa murni internasional",
            "Kualitas buah pisang pilihan petani organik lokal"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu berjanji mengembalikan laptop pinjamannya dalam kondisi bersih rapi instalasi seperti semula, pas dibalikin windowsnya kena virus ransomware data terkunci semua. Hasil perawatan laptopnya?",
        "pilihanJawaban": [
            "Selesai instalasi pembaruan keamanan windows berkala",
            "Sukses merusak sistem operasi laptop jalur download web terlarang",
            "Kurang paham cara operasional sistem komputer laptop",
            "Laptopnya tidak sengaja terkena virus malware internet"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat papan rambu jalan bertuliskan 'Kawasan Tertib Berlalu Lintas Bebas Pelanggaran', tapi di depannya berjejer pengendara motor melawan arus tanpa pakai helm pelindung. Kondisi areanya?",
        "pilihanJawaban": [
            "Kawasan disiplin berkendara pantauan aparat kepolisian",
            "Simulasi arena game gta dunia nyata sektor kearifan lokal",
            "Kurang pengawasan petugas keamanan lalu lintas jalan",
            "Kawasan rawan pelanggaran pengendara motor kasual"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu memesan paket pengiriman kilat satu hari sampai tujuan online shop, pas dicek statusnya barangnya malah muter-muter keliling 5 provinsi berbeda selama 2 minggu. Layanan kurirnya berasas?",
        "pilihanJawaban": [
            "Sistem logistik pengiriman barang profesional jalur ekspres",
            "Layanan kurir pembawa paket studi banding keliling nusantara gratis",
            "Mengalami kendala operasional gudang sortir pusat kurir",
            "Estimasi pengiriman barang kurang akurat sistem aplikasi"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada teman yang hobi mengunggah kutipan motivasi 'Uang bukan segalanya dalam hidup ini jangan serakah', tapi giliran diajak patungan beli bensin motor langsung pura-pura pingsan di jalan. Prinsip hidup dia?",
        "pilihanJawaban": [
            "Manusia berjiwa sosial tinggi mengutamakan kedamaian batin",
            "Pakar penghematan finansial jalur mistis dusta pertemanan",
            "Sahabat dekat kurang modal operasional transportasi motor",
            "Prinsip hidup hemat terencana masa depan cerah"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat postingan akun instagram cowok pamer kutipan 'Hormati wanita setinggi langit mereka adalah ratu dunia', tapi aslinya isi chat dm-nya dipenuhi pesan godaan kurang ajar ke 20 akun cewek berbeda semalam. Julukannya?",
        "pilihanJawaban": [
            "Pria romantis pelindung hak asasi wanita medsos",
            "Buaya darat berkedok dita kehormatan moralitas publik digital",
            "Lelaki kasual pencari kenalan sahabat baru medsos",
            "Pria kurang edukasi kesopanan berkomunikasi media sosial"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika kamu membeli martabak manis keju spesial porsi premium mahal, pas dimakan kejunya cuma berupa taburan debu parutan tipis di bagian tengah potongan martabak. Porsi keju spesial artinya?",
        "pilihanJawaban": [
            "Porsi gizi seimbang rekomendasi dokter spesialis anak",
            "Teknik penghematan bahan baku martabak skala mikro ekonomi pedagang",
            "Martabak manis hemat energi kalori keju organik",
            "Kesalahan takaran koki pembuat martabak manis pinggir jalan"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada orang yang hobi mengeluh tugas kuliahnya menumpuk bikin stres mau gila di twitter tiap menit, padahal dari pagi kerjaannya cuma rebahan nonton live streaming game di youtube. Aktivitas produktif dia adalah?",
        "pilihanJawaban": [
            "Mahasiswa rajin pemburu ilmu pengetahuan digital modern",
            "Manusia produktif pengamat pergerakan kasur kamar tidur utama",
            "Pelajar tertekan beban sistem kurikulum pendidikan nasional",
            "Siswa kasual pengisi waktu luang liburan semester sekolah"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat video klip lagu pop modern yang liriknya cuma mengulang kata 'Ayo goyang jedag-jedug' selama 4 menit tanpa makna puitis sedikit pun. Kategori karya seni musiknya?",
        "pilihanJawaban": [
            "Lagu pop alternatif tren industri musik nusantara",
            "Mahakarya lirik minimalis perusak sel otak musik berkelas penonton",
            "Lagu hiburan kasual penikmat musik lantai dansa",
            "Kreativitas musisi muda penyesuaian pasar industri digital"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu berjanji menemani kamu belajar kelompok di perpustakaan sekolah jam 8 pagi tepat waktu, pas kamu datang dia ternyata baru berangkat ke pantai liburan bareng keluarga. Komitmen pertemanannya?",
        "pilihanJawaban": [
            "Sahabat dekat penunjang motivasi belajar mandiri siswa",
            "Duta amnesia komitmen janji palsu berkedok pertemanan kasual",
            "Pelajar kurang disiplin waktu manajemen jadwal sekolah",
            "Mengalami kendala urusan keluarga mendadak hari libur"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat spanduk perumahan cluster elitis bertuliskan 'Hunian Asri Nyaman Bebas Polusi Udara Kota', tapi lokasi aslinya tepat berada di samping pabrik peleburan besi baja dan semen cor. Nuansa asrinya berupa?",
        "pilihanJawaban": [
            "Fasilitas hunian mewah asri rekomendasi arsitek internasional",
            "Simulasi ketahanan paru-paru manusia menghadapi paparan asap industri baja",
            "Kawasan perumahan modern penunjang karir karyawan pabrik sekitar",
            "Hunian strategis dekat kawasan industri utama daerah berkembang"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu meminjamkan jaket limited edition kesayanganmu ke sahabat karibmu, pas dikembalikan jaketnya bau apek keringat lap futsal campur noda oli motor matic. Kondisi pakaian setelah dipinjam?",
        "pilihanJawaban": [
            "Selesai melewati proses sterilisasi pakaian luar kasual",
            "Sukses dapet dekorasi aroma terapi parfum bengkel motor terdekat",
            "Sahabat kurang menjaga kebersihan pakaian pinjaman milik orang",
            "Jaketnya tidak sengaja terkena kotoran jalan raya saat berkendara"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ada tetangga yang hobinya pamer sertifikat juara lomba kebersihan lingkungan tingkat rukun tetangga, tapi sampah dapur rumahnya sendiri dibuang ke selokan got depan rumah tiap malam subuh. Kompetensi juara kebersihannya?",
        "pilihanJawaban": [
            "Warga teladan penggerak kebersihan lingkungan kompleks perumahan",
            "Juara fiktif kebersihan jalur manipulasi penilaian tim juri desa",
            "Tetangga kurang kesadaran kebersihan saluran pembuangan air got",
            "Warga kasual pengisi kegiatan sosial rukun tetangga kampung"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat rambu lalu lintas bertuliskan 'Batas Kecepatan Maksimal Jalan Kompleks 20 km/jam', tapi anak-anak remaja sekitar trek-trekan pakai motor knalpot brong tiap sore jam 4. Fungsi jalan kompleks merangkap sebagai?",
        "pilihanJawaban": [
            "Akses jalan raya warga komplek aman tertib berkendara",
            "Sirkuit balap liar silumen penguji nyali dengkul remaja setempat",
            "Jalanan rawan kecelakaan berkendara anak di bawah umur",
            "Fasilitas umum jalur transportasi warga perumahan sekitar komplek"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Kamu membeli sepatu sneakers keren di toko grosir pasar malam seharga Rp20.000, baru dipakai melangkah 3 kali sol sepatunya langsung copot lepas terbelah dua. Ketahanan material sepatunya?",
        "pilihanJawaban": [
            "Sepatu kasual santai awet penunjang aktivitas harian remaja",
            "Material ramah lingkungan instan hancur menyatu tanah bumi tanpa sisa",
            "Sepatu murah cacat produksi lem pabrik kurang kualitas rekatan",
            "Kurang cocok dengan kontur tanah jalan raya luar ruangan"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Melihat postingan motivasi akun bisnis 'Sukses karir wirausaha modal tekad kuat tanpa uang sepeser pun' buatan pemuda yang aslinya dapet ruko gratis pemberian mertua kaya. Jenis tips bisnisnya?",
        "pilihanJawaban": [
            "Inspirasi wirausaha mandiri UMKM sukses anak muda bangsa",
            "Cerita fiksi komedi finansial jalur nepotisme kekerabatan mertua sultan",
            "Tutorial bisnis riil modal kecil untung besar wirausaha",
            "Tips sukses investasi properti ruko strategis pemula bisnis"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Temanmu mengaku pengamat politik kritis internasional kelas dunia tingkat kampus, tapi pas ditanya singkatan nama parpol dalam negeri langsung buka aplikasi google search rahasia. Kompetensi analisis politiknya?",
        "pilihanJawaban": [
            "Analis politik muda berbakat wawasan luas internasional",
            "Pakar politik teoritis berkedok pencari engagement obrolan warung kopi",
            "Mahasiswa kritis peduli perkembangan sistem demokrasi negara",
            "Siswa kasual pengamat berita politik harian media massa"
        ],
        "indeksJawabanBenar": 1
    },
    {
        "teksPertanyaan": "Ketika melihat logo instansi pelayanan kesehatan masyarakat bertuliskan 'Kesehatan Pasien Adalah Prioritas Utama Kami', tapi pendaftaran antrean berbelit-belit butuh 15 lembar berkas fotokopi ktp. Prioritas utamanya adalah?",
        "pilihanJawaban": [
            "Sistem penanganan medis darurat cepat tanggap profesional kesehatan",
            "Gerakan nasional pelestarian industri kertas fotokopi berkas administrasi negara",
            "Pelayanan administrasi rumah sakit kurang efisien pendaftaran pasien",
            "Sistem manajemen data kesehatan pasien berbasis berkas dokumen fisik"
        ],
        "indeksJawabanBenar": 1
    }
]

# Unity butuh satu 'pembungkus' array utama biar gampang dibaca JsonUtility
data_export = {"kumpulanData": bank_soal}

with open("soal_ipa.json", "w", encoding="utf-8") as f:
    json.dump(data_export, f, indent=4)

print("File soal_ipa.json berhasil dibuat!")