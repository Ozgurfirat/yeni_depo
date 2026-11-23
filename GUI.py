
import tkinter as tk
from tkinter import ttk
from Sipariş_classı import Sipariş

class Ana_ekran:
    def __init__(self):
        self.ekran = tk.Tk()
        en = self.ekran.winfo_screenwidth()
        boy = self.ekran.winfo_screenheight()

        self.ekran.geometry(f"{en}x{boy}+0+0")
        self.ekran.title("_ _ _ _    Sipariş ve Üretim Takip Otomasyonu    _ _ _ _")

        # RENK PALETİ
        self.arka_plan = "#171B24"
        self.cerceve_renk = "#222936"
        self.giris_renk = "#303947"
        self.yazi_renk = "#E8EDF5"
        self.ikincil_yazi = "#AAB5C5"
        self.buton_renk = "#2864A5"
        self.buton_hover = "#3989D6"
        self.buton_basili = "#159A9C"

        self.ekran.configure(bg=self.arka_plan)

        self.orta_font = ("Helvetica bold", 17)
        self.k_font = ("Helvetica", 15)
        self.b_font = ("Helvetica bold", 22)
        self.mini_font = ("Helvetica bold", 13)

        # TKİNTER DEĞİŞKENLERİ TANIMLANIYOR
        self.gln_mlz_hmmd_değ = tk.StringVar()
        self.gln_mlz_türü_değ = tk.StringVar()
        self.gln_mlz_tonaj_değ = tk.StringVar()
        self.iş_alış_tarihi_değ = tk.StringVar()
        self.sorumlu_kişi_değ = tk.StringVar()
        self.sorumlu_iletişim_değ = tk.StringVar()
        self.iş_durumu_değ = tk.BooleanVar()

        self.gdn_mlz_türü_değ = tk.StringVar()
        self.gdn_mlz_tonaj_değ = tk.StringVar()
        self.iş_teslim_tarihi_değ = tk.StringVar()
        self.karşı_kişi_değ = tk.StringVar()
        self.karşı_sorumlu_iletişim_değ = tk.StringVar()

        # COMBOBOX LİSTELERİ
        self.hammade_listesi = [
            "Bakır", "Demir", "Çelik", "Aluminyum",
            "Galvaniz", "Krom", "Siyah Demir"
        ]

        self.mlz_türü_listesi = [
            "Sac", "Boru", "Profil", "Oksijen Kesim", "Lazer Kesim"
        ]

        # COMBOBOX STİLİ
        stil = ttk.Style()
        stil.theme_use("clam")

        stil.configure(
            "TCombobox",
            fieldbackground=self.giris_renk,
            background=self.cerceve_renk,
            foreground=self.yazi_renk,
            arrowcolor=self.yazi_renk,
            bordercolor=self.cerceve_renk,
            padding=8,
            font=self.k_font
        )

        stil.map(
            "TCombobox",
            fieldbackground=[("readonly", self.giris_renk)],
            foreground=[("readonly", self.yazi_renk)],
            selectbackground=[("readonly", self.buton_renk)],
            selectforeground=[("readonly", "white")]
        )

        # ANA EKRAN SÜTUN VE SATIR AYARLARI
        self.ekran.grid_columnconfigure((0, 1), weight=1)
        self.ekran.grid_rowconfigure(1, weight=1)

        # ŞİRKET ADI
        self.firma_adı_label = self.label_oluştur(
            self.ekran, str(Sipariş.kuruluş_adı), 0, 0
        )

        self.firma_adı_label.grid_configure(
            columnspan=2, sticky=tk.EW, pady=20
        )

        self.firma_adı_label.config(
            font=self.b_font,
            fg="#55B8FF",
            bg=self.arka_plan
        )

        # GELEN MALZEME ÇERÇEVESİ
        self.gelen_çerçeve = tk.LabelFrame(
            self.ekran,
            text=" GELEN MALZEME BİLGİLERİ ",
            labelanchor=tk.N,
            font=self.mini_font,
            bd=2,
            relief="groove",
            bg=self.cerceve_renk,
            fg="#55B8FF",
            padx=15,
            pady=15
        )

        self.gelen_çerçeve.grid(
            row=1, column=0, padx=20, pady=15,
            ipadx=10, ipady=10, sticky=tk.NSEW
        )

        self.gelen_çerçeve.grid_columnconfigure(1, weight=1)

        self.gln_mlz_hmmd_label = self.label_oluştur(
            self.gelen_çerçeve, "Gelen Malzeme Hammaddesi:", 0, 0
        )

        self.gln_mlz_hmmd_combo = ttk.Combobox(
            self.gelen_çerçeve,
            values=self.hammade_listesi,
            textvariable=self.gln_mlz_hmmd_değ,
            font=self.k_font,
            style="TCombobox",
            state="readonly",
            width=25
        )

        self.gln_mlz_hmmd_combo.grid(
            row=0, column=1, padx=10, pady=10, sticky=tk.EW
        )

        self.gln_mlz_türü_label = self.label_oluştur(
            self.gelen_çerçeve, "Gelen Malzeme Türü:", 1, 0
        )

        self.gln_mlz_türü_combo = ttk.Combobox(
            self.gelen_çerçeve,
            values=self.mlz_türü_listesi,
            textvariable=self.gln_mlz_türü_değ,
            font=self.k_font,
            style="TCombobox",
            state="readonly",
            width=25
        )

        self.gln_mlz_türü_combo.grid(
            row=1, column=1, padx=10, pady=10, sticky=tk.EW
        )

        self.gln_mlz_tonaj_label = self.label_oluştur(
            self.gelen_çerçeve, "Gelen Malzeme Tonaj:", 2, 0
        )

        self.gln_mlz_tonaj_giriş = self.giriş_oluştur(
            self.gelen_çerçeve, self.gln_mlz_tonaj_değ, 2, 1
        )

        self.iş_alış_tarihi_label = self.label_oluştur(
            self.gelen_çerçeve, "İş Alış Tarihi:", 3, 0
        )

        self.iş_alış_tarihi_giriş = self.giriş_oluştur(
            self.gelen_çerçeve, self.iş_alış_tarihi_değ, 3, 1
        )

        self.sorumlu_kişi_label = self.label_oluştur(
            self.gelen_çerçeve, "Sorumlu Kişi:", 4, 0
        )

        self.sorumlu_kişi_giriş = self.giriş_oluştur(
            self.gelen_çerçeve, self.sorumlu_kişi_değ, 4, 1
        )

        self.sorumlu_kişi_iletişim_label = self.label_oluştur(
            self.gelen_çerçeve, "Sorumlu Kişi İletişim:", 5, 0
        )

        self.sorumlu_kişi_iletişim_giriş = self.giriş_oluştur(
            self.gelen_çerçeve, self.sorumlu_iletişim_değ, 5, 1
        )

        # GİDEN MALZEME ÇERÇEVESİ
        self.giden_çerçeve = tk.LabelFrame(
            self.ekran,
            text=" GİDEN MALZEME BİLGİLERİ ",
            labelanchor=tk.N,
            font=self.mini_font,
            bd=2,
            relief="groove",
            bg=self.cerceve_renk,
            fg="#55B8FF",
            padx=15,
            pady=15
        )

        self.giden_çerçeve.grid(
            row=1, column=1, padx=20, pady=15,
            ipadx=10, ipady=10, sticky=tk.NSEW
        )

        self.giden_çerçeve.grid_columnconfigure(1, weight=1)

        self.gdn_mlz_türü_label = self.label_oluştur(
            self.giden_çerçeve, "Giden Malzeme Türü:", 0, 0
        )

        self.gdn_mlz_türü_combo = ttk.Combobox(
            self.giden_çerçeve,
            values=self.mlz_türü_listesi,
            textvariable=self.gln_mlz_türü_değ,
            font=self.k_font,
            style="TCombobox",
            state="readonly",
            width=25
        )

        self.gdn_mlz_türü_combo.grid(
            row=0, column=1, padx=10, pady=10, sticky=tk.EW
        )

        self.gdn_mlz_tonaj_label = self.label_oluştur(
            self.giden_çerçeve, "Giden Malzeme Tonaj:", 1, 0
        )

        self.gdn_mlz_tonaj_giriş = self.giriş_oluştur(
            self.giden_çerçeve, self.gdn_mlz_tonaj_değ, 1, 1
        )

        self.iş_teslim_tarihi_label = self.label_oluştur(
            self.giden_çerçeve, "İş Teslim Tarihi:", 2, 0
        )

        self.iş_teslim_tarihi_giriş = self.giriş_oluştur(
            self.giden_çerçeve, self.iş_teslim_tarihi_değ, 2, 1
        )

        self.karşı_sorumlu_label = self.label_oluştur(
            self.giden_çerçeve, "Sorumlu (Karşı Taraf):", 3, 0
        )

        self.karşı_sorumlu_giriş = self.giriş_oluştur(
            self.giden_çerçeve, self.karşı_kişi_değ, 3, 1
        )

        self.karşı_sorumlu_iletişim_label = self.label_oluştur(
            self.giden_çerçeve, "Sorumlu İletişim:", 4, 0
        )

        self.karşı_sorumlu_iletişim_giriş = self.giriş_oluştur(
            self.giden_çerçeve, self.karşı_sorumlu_iletişim_değ, 4, 1
        )

        self.iş_teslim_durumu_label = self.label_oluştur(
            self.giden_çerçeve, "İş Teslim Durumu:", 5, 0
        )

        self.iş_devam_rdbtn = tk.Radiobutton(
            self.giden_çerçeve,
            text="Devam Ediyor",
            font=self.k_font,
            variable=self.iş_durumu_değ,
            value=False,
            bg=self.cerceve_renk,
            fg=self.yazi_renk,
            selectcolor=self.giris_renk,
            activebackground=self.cerceve_renk,
            activeforeground="#55B8FF"
        )

        self.iş_devam_rdbtn.grid(
            row=5, column=1, padx=10, pady=5, sticky=tk.W
        )

        self.iş_teslim_rdbtn = tk.Radiobutton(
            self.giden_çerçeve,
            text="Teslim Edildi",
            font=self.k_font,
            variable=self.iş_durumu_değ,
            value=True,
            bg=self.cerceve_renk,
            fg=self.yazi_renk,
            selectcolor=self.giris_renk,
            activebackground=self.cerceve_renk,
            activeforeground="#55B8FF"
        )

        self.iş_teslim_rdbtn.grid(
            row=6, column=1, padx=10, pady=(0, 10), sticky=tk.W
        )

        # TUŞ ÇERÇEVESİ
        tuş_çerçevesi = tk.Frame(
            self.ekran,
            bg=self.cerceve_renk,
            bd=2,
            relief="groove",
            padx=20,
            pady=10
        )

        tuş_çerçevesi.grid(
            row=2, column=0, columnspan=2,
            padx=20, pady=15, sticky=tk.EW
        )

        tuş_çerçevesi.grid_columnconfigure((0, 1), weight=1)

        self.geri_tuşu = self.tuş_oluştur(
            tuş_çerçevesi, "◀  Geri", 0, 0
        )

        self.ileri_tuşu = self.tuş_oluştur(
            tuş_çerçevesi, "İleri  ▶", 0, 1
        )

        üçlü_çerçeve = tk.Frame(
            tuş_çerçevesi,
            bg=self.cerceve_renk
        )

        üçlü_çerçeve.grid(
            row=1, column=0, columnspan=2,
            pady=5
        )

        üçlü_çerçeve.grid_columnconfigure((0, 1, 2), weight=1)

        self.ekle_tuşu = self.tuş_oluştur(
            üçlü_çerçeve, "＋  Kayıt Ekle", 0, 0
        )

        self.güncelle_tuşu = self.tuş_oluştur(
            üçlü_çerçeve, "✎  Kayıt Güncelle", 0, 1
        )

        self.sil_tuşu = self.tuş_oluştur(
            üçlü_çerçeve, "✕  Kayıt Sil", 0, 2
        )

        self.excele_gönder_tuşu = self.tuş_oluştur(
            tuş_çerçevesi, "Excel'e Gönder", 2, 0
        )

        self.arşiv_görüntüle_tuşu = self.tuş_oluştur(
            tuş_çerçevesi, "Arşiv Görüntüle", 2, 1
        )

    # LABEL OLUŞTURAN METOT
    def label_oluştur(self, ekran_adı, yazı, satır, sütun):
        etiket = tk.Label(
            ekran_adı,
            text=yazı,
            font=self.k_font,
            bg=self.cerceve_renk,
            fg=self.yazi_renk
        )

        etiket.grid(
            row=satır,
            column=sütun,
            padx=10,
            pady=12,
            sticky=tk.E
        )

        return etiket

    # ENTRY OLUŞTURAN METOT
    def giriş_oluştur(self, ekran, değişken, satır, sütun):
        giriş = tk.Entry(
            ekran,
            textvariable=değişken,
            font=self.k_font,
            width=30,
            bg=self.giris_renk,
            fg=self.yazi_renk,
            insertbackground="white",
            relief="flat",
            bd=5,
            highlightthickness=1,
            highlightbackground="#46546A",
            highlightcolor="#55B8FF"
        )

        giriş.grid(
            row=satır,
            column=sütun,
            padx=(0, 10),
            pady=10,
            sticky=tk.EW
        )

        return giriş

    # TUŞ OLUŞTURAN METOT
    def tuş_oluştur(self, ekran, yazı, satır, sütun):
        tuş = tk.Button(
            ekran,
            text=yazı,
            font=self.orta_font,
            bg=self.buton_renk,
            fg="white",
            activebackground=self.buton_basili,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=12,
            cursor="hand2",
            width=17
        )

        tuş.grid(
            row=satır,
            column=sütun,
            padx=12,
            pady=12,
            sticky=tk.EW
        )

        # FARE ÜZERİNE GELİNCE RENK DEĞİŞİMİ
        tuş.bind(
            "<Enter>",
            lambda olay: tuş.config(bg=self.buton_hover)
        )

        # FARE AYRILINCA ESKİ RENGE DÖNÜŞ
        tuş.bind(
            "<Leave>",
            lambda olay: tuş.config(bg=self.buton_renk)
        )

        # TUŞA BASILINCA RENK DEĞİŞİMİ
        tuş.bind(
            "<ButtonPress-1>",
            lambda olay: tuş.config(bg=self.buton_basili)
        )

        # TUŞ BIRAKILINCA HOVER RENGİNE DÖNÜŞ
        tuş.bind(
            "<ButtonRelease-1>",
            lambda olay: tuş.config(bg=self.buton_hover)
        )

        return tuş

    def ekran_döngü(self):
        self.ekran.mainloop()
