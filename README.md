# Password Manager / مدير كلمات المرور

برنامج بسيط وفعال لإدارة كلمات المرور مكتوب بلغة Python. يسمح البرنامج للمستخدمين بإما إدخال كلمة مرور خاصة بهم أو توليد كلمة مرور عشوائية. يقوم البرنامج بفحص قوة كلمة المرور وتجزئتها باستخدام خوارزمية SHA-256. وأخيرًا، يتم حفظ كلمة المرور المجزأة في ملف.

A simple and efficient Password Manager written in Python. The program allows users to either input their own password or generate a random password. It checks the strength of the password and hashes it using the SHA-256 algorithm. Finally, the hashed password is saved to a file.

## الميزات / Features

- **تجزئة كلمة المرور / Password Hashing**: تجزئة كلمة المرور باستخدام خوارزمية SHA-256.
- **توليد كلمة المرور / Password Generation**: توليد كلمة مرور عشوائية بطول محدد.
- **فحص قوة كلمة المرور / Password Strength Checking**: فحص قوة كلمة المرور استنادًا إلى معايير محددة.
- **تأكيد كلمة المرور / Password Confirmation**: التأكد من صحة كلمة المرور من خلال طلبها مرتين من المستخدم.
- **تخزين كلمة المرور / Password Storage**: تخزين كلمة المرور المجزأة في ملف.

## كيفية الاستخدام / Usage

1. **استنساخ المستودع / Clone the repository**:
    ```bash
    git clone https://github.com/Haiedr55/passwordmanger
    cd passwordmanager
    pip/pip3 install requirements.txt

2. تشغيل البرنامج / Run the program:
        python main.py
    

3. اتباع التعليمات / Follow the prompts:
    - سيطلب منك البرنامج إما إدخال كلمة مرور خاصة بك أو توليد كلمة مرور عشوائية.
    - إذا اخترت إدخال كلمة المرور الخاصة بك، سيتعين عليك إدخالها مرتين للتأكيد.
    - إذا اخترت توليد كلمة مرور، ستحتاج إلى تحديد الطول المطلوب.
    - سيقوم البرنامج بعد ذلك بفحص قوة كلمة المرور وتجزئتها باستخدام SHA-256.
    - سيتم عرض كلمة المرور المجزأة وحفظها في ملف يسمى hashed_passwords.txt.

## المساهمة / Contributing

إذا كنت ترغب في المساهمة في هذا المشروع، يرجى نسخ المستودع وإرسال طلب السحب. نحن نرحب بجميع المساهمات!

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!
```
