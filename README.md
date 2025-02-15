# CookBox

## 📌 რეცეპტების ბაზა
CookBox არის რეცეპტების მართვის აპლიკაცია, რომელიც შეიცავს სხვადასხვა ქვეყნის კერძების ბაზას.

### 📂 მონაცემთა ბაზის სტრუქტურა
- **ID**
- **კერძის დასახელება**
- **კერძის დასახელება ლათინური ასოებით**
- **კატეგორია**
- **ქვეყანა**
- **შემადგენელი ინგრედიენტები**
- **ინგრედიენტების სახელწოდება რაოდენობასთან ერთად**
- **📖 ინსტრუქცია** (მომზადების მოკლე ინსტრუქცია)
- **⏳ მომზადების დრო**

> **ℹ️ შენიშვნა:** რეცეპტების რაოდენობა შესაძლოა შეიცვალოს. ბაზაში შეიძლება განმეორდეს ერთი და იგივე კერძი, თუ მას აქვს განსხვავებული მომზადების ინსტრუქცია.

---

## 🏠 აპლიკაციის მთავარი გვერდი
მთავარი გვერდი შეიცავს:
- 🔍 **საძიებო ველს**
- 📂 **კატეგორიების ღილაკებს**:
  - 🍰 **დესერტები**
  - 🍲 **კერძები**
  - 🥪 **წასახემსებელი**

### 🔎 კატეგორიების მიხედვით ძიება
კატეგორიაზე დაკლიკებისას იხსნება შესაბამისი გვერდი, სადაც ბაზიდან გამოჩნდება ამ კატეგორიის შესაბამისი პროდუქტები.

### 🔎 საძიებო ველის გამოყენება
მომხმარებლის მიერ კერძის სახელის შეყვანის შემთხვევაში პროგრამა გამოიტანს ყველა შესაბამის ინფორმაციას _(გარდა ID ველის)_.

### 🎲 რეცეპტების შემთხვევითი შეთავაზება
აპლიკაცია აჩვენებს შემთხვევითად (random) გენერირებულ რეცეპტებს, რომლებიც შეიცავენ:
- 📌 **კერძის სახელს**
- 📖 **ინსტრუქციას**
- ⏳ **მომზადების დროს**
- 🖼 **ფოტოს**

---

## 🌍 სხვადასხვა ქვეყნების სამზარეულო
მთავარ გვერდზე განთავსდება ღილაკი **"🌎 სხვადასხვა ქვეყნების სამზარეულო"**, რომელზეც დაკლიკებისას გაიხსნება ახალი გვერდი, სადაც მომხმარებელი აირჩევს ქვეყანას.

მაგალითად:
- 🇬🇪 **საქართველო**
- 🇮🇹 **იტალია**
- 🇫🇷 **საფრანგეთი**
- 🇯🇵 **იაპონია**

ყოველ ქვეყანას ექნება შესაბამისი სამზარეულოს გამორჩეული კერძის ფოტო, რაც გაამარტივებს ვიზუალურ აღქმას. მომხმარებლის მიერ ქვეყნის არჩევის შემდეგ, პროგრამა ბაზიდან მოიძიებს და გამოიტანს ამ ქვეყნის შესაბამის კერძებს.

---

## 🥦 ინგრედიენტების მიხედვით ძიება
მომხმარებელს შეეძლება აირჩიოს კონკრეტული ინგრედიენტები, რის შემდეგაც პროგრამა მოძებნის და გამოიტანს რეცეპტებს, რომლებიც შეიცავს ამ ინგრედიენტებს.

