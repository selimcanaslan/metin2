def combo_values(self):
    self.item_combo.setPlaceholderText("İtem Seç")
    self.item_combo_2.setPlaceholderText("İtem Seç")
    self.item_combo_3.setPlaceholderText("İtem Seç")
    self.item_combo_4.setPlaceholderText("İtem Seç")
    self.item_combo_5.setPlaceholderText("İtem Seç")
    self.item_combo_6.setPlaceholderText("İtem Seç")
    self.item_combo_7.setPlaceholderText("İtem Seç")
    self.item_combo_8.setPlaceholderText("İtem Seç")
    self.item_combo_9.setPlaceholderText("İtem Seç")
    self.item_combo_10.setPlaceholderText("İtem Seç")
    self.item_combo_11.setPlaceholderText("Map Seç")
    item_names = list()
    item_names.append("Metin Sandığı")
    item_names.append("Cor Draconis")
    item_names.append("Yükseltme Sand.")
    item_names.append("Efsun Nesnesi")
    item_names.append("Eğitim Sand.")
    item_names.append("Süs Taşı")
    item_names.append("Büyülü Metal")
    item_names.append("Nemere Bileti")
    item_names.append("Razador Bileti")
    item_names.append("İstiridye")
    for item_name in item_names:
        self.item_combo.addItem(item_name)
        self.item_combo_2.addItem(item_name)
        self.item_combo_3.addItem(item_name)
        self.item_combo_4.addItem(item_name)
        self.item_combo_5.addItem(item_name)
        self.item_combo_6.addItem(item_name)
        self.item_combo_7.addItem(item_name)
        self.item_combo_8.addItem(item_name)
        self.item_combo_9.addItem(item_name)
        self.item_combo_10.addItem(item_name)
    map_names = list()
    map_names.append("Ejderha Ateşi Burnu")
    map_names.append("Nefrit")
    map_names.append("Yıldırım")
    map_names.append("Guatama")
    map_names.append("Büyülü Orman")
    for maps in map_names:
        self.item_combo_11.addItem(maps)