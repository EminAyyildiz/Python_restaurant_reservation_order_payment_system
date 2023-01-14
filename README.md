# Python_restaurant_reservation_order_payment_system



# Bu projenin temel amacı restoranlarda kullanılan rezervasyon oluşturma, masa numarasına göre sipariş alma ve ödeme kanalları aracılığla toplam yemek ücretini kullanıcıdan almaktır. Bu projede öncelikle güvenlik açısından sisteme erişim için bir username ve password tanımladık. Kullanıcı bu username ve password ile sisteme giriş sağladığında kullanıcıyı bir menü karşılamaktadır. Bu menünün içeriğini anlatacak olursak: 1-Make reservation 2-Check Avaibility Reservation 3-Order 3-Select Payment Method 5-EXIT olmak üzere5 kısımdan oluşur. Bu bölümlerin görevlerinden bahsetmek gerekirse: 1- Bu seçenek ile öncelikle müşteriye kaç kişilik bir masa istediği sorulur. Sistemde 2-4-6 kişilik 10 ar adet masa bulunmaktadır. Daha sonra müşteri masa numarası seçmektedir. Eğer ki masa boş ise rezervasyon müşterinin ismi girilerek tamamlanır. 2-Bu seçeneğin temel amacı boş masaları görüntülemektir. Bu seçnçenek ile kaçar kişilik masalardan kaç adet masa boş bunu görebilirsiniz. 3-Bu seçenek ile amaç müşterinin siparişlerini sisteme girmektir. Öncelikle kullanıcıdan hangi masa için sipariş girileceği bilgisi alınır eğer ki masada müşteri yok ise hatalı giriş yapıldı yazısını ekrana yazdırır. Eğer ki uygun bir masa numarası girilirse kullanıcıya bir menü ekranı çıkar ve ürünlerin yanında fiyatlarıyla birlikte kullanıcıya sunulur. Kullanıcı buradan siparişleri yazarak girer eğer ki daha fazla sipariş eklemek istiyorsa sorulan soruya yes eklemek istemiyorsa no cevabı ile yoluna devam eder. 4-Bu seçenek ile amaç ödeme yapmaktır. Bu seçeneğe ilk olarak giriş yapıldığında kullanıcıdan yine masa numarası istenmektedir. Eğer ki masa numarası doğru ise o masanın borcu ekrana yazdırılır. Daha sonra kullanıcıya 3 adet olmak üzere ( KREDİ, PAYPAL, CASH) ödeme yöntemi sunulur. Kullanıcın seçeceği ödeme yöntemine göre sistem kart numarası veya şifre isteyerek ödemeyi kabul eder. Bu noktada girilen kart numarası 16 haneden az olmamalı ve girilen şifre uzunluğu 4 haneli olmalı aksi taktirde sistem ödemeyi kabul etmemektedir. Müşteri ödemeyi başarıyla tamamladıktan sonra müşterinin masası boşaltılır ve borcu 0 a eşitlenir. 5- Bu seçenek ile sistemden çıkış yapılmaktadır. Kullanıcı bu seçeneğe bastığında tekrardan şifre giriş ekranına gelir. Şifre giriş ekranında kullanıcı adı veya şifre bölümlerinden ikisinden birine "q" veya "Q" harfleri girildiğinde direkt olarak kod çalışmayı durdurur.




# The main purpose of this project is to collect the total meal fee from the user through the means of creating reservations, taking orders by table number and payment channels used in restaurants. In this project, we first defined a username and password for accessing the system in terms of security. When the user logs in to the system with this username and password, a menu welcomes the user. If we explain the content of this menu: 1-Make reservation 2-Check Avaibility Reservation 3-Order 3-Select Payment Method 5-EXIT consists of 5 parts. To talk about the duties of these departments: 1- With this option, the customer is first asked how many people a table he wants. There are 10 tables for 2-4-6 people in the system. Then the customer chooses the table number. If the table is empty, the reservation is completed by entering the customer's name. 2-The main purpose of this option is to display empty tables. With this option, you can see how many tables are empty from the tables for how many people. 3- With this option, the aim is to enter the customer's orders into the system. First of all, information is obtained from the user for which table the order will be entered, and if there is no customer at the table, it prints the message that the wrong entry was made on the screen. If a suitable table number is entered, a menu screen appears and presented to the user with the prices next to the products. The user enters the orders here by typing, if he wants to add more orders, if he does not want to add yes to the question asked, he continues on his way with the answer no. 4-The purpose of this option is to make a payment. When logging in to this option for the first time, the user is asked for the table number again. If the table number is correct, the debt of that table is printed on the screen. Then the user is presented with 3 payment methods (CREDIT, PAYPAL, CASH). According to the payment method chosen by the user, the system accepts the payment by requesting a card number or password. At this point, the card number entered should not be less than 16 digits and the length of the entered password should be 4 digits, otherwise the system does not accept the payment. After the customer successfully completes the payment, the customer's desk is cleared and the debt is set to 0. 5- With this option, the system is logged out. When the user presses this option, he/she comes to the password entry screen again. When the letters "q" or "Q" are entered in either of the user name or password sections on the password entry screen, the code stops working directly.




# Der Hauptzweck dieses Projekts besteht darin, die gesamte Essensgebühr vom Benutzer durch die Erstellung von Reservierungen, die Entgegennahme von Bestellungen nach Tischnummer und die in Restaurants verwendeten Zahlungskanäle einzuziehen. In diesem Projekt haben wir aus Sicherheitsgründen zunächst einen Benutzernamen und ein Passwort für den Zugriff auf das System definiert. Wenn sich der Benutzer mit diesem Benutzernamen und Passwort beim System anmeldet, wird der Benutzer von einem Menü begrüßt. Wenn wir den Inhalt dieses Menüs erklären: 1-Reservierung vornehmen 2-Verfügbarkeit prüfen Reservierung 3-Bestellung 3-Zahlungsmethode auswählen 5-EXIT besteht aus 5 Teilen. Um über die Aufgaben dieser Abteilungen zu sprechen: 1- Bei dieser Option wird der Kunde zuerst gefragt, wie viele Personen einen Tisch haben möchten. Es gibt 10 Tische für 2-4-6 Personen in der Anlage. Dann wählt der Kunde die Tischnummer. Ist der Tisch leer, wird die Reservierung durch Eingabe des Kundennamens abgeschlossen. 2-Der Hauptzweck dieser Option ist die Anzeige leerer Tabellen. Mit dieser Option können Sie sehen, wie viele Tische für wie viele Personen leer sind. 3- Ziel dieser Option ist es, die Bestellungen des Kunden in das System einzugeben. Zunächst wird vom Benutzer die Information eingeholt, für welchen Tisch die Bestellung eingegeben wird, und wenn kein Kunde am Tisch ist, druckt es die Meldung, dass eine falsche Eingabe auf dem Bildschirm vorgenommen wurde. Wenn eine passende Tischnummer eingegeben wird, erscheint ein Menübildschirm und wird dem Benutzer mit den Preisen neben den Produkten präsentiert. Der Benutzer gibt die Aufträge ein, indem er hier eintippt, wenn er weitere Aufträge hinzufügen möchte, und wenn er der gestellten Frage kein Ja hinzufügen möchte, fährt er mit der Antwort Nein fort. 4-Der Zweck dieser Option ist die Zahlung. Beim erstmaligen Einloggen in diese Option wird der Benutzer erneut nach der Tischnummer gefragt. Wenn die Tischnummer korrekt ist, wird die Schuld dieses Tisches auf dem Bildschirm gedruckt. Dann werden dem Benutzer 3 Zahlungsmethoden (KREDIT, PAYPAL, BAR) präsentiert. Je nach der vom Benutzer gewählten Zahlungsmethode akzeptiert das System die Zahlung, indem es eine Kartennummer oder ein Passwort anfordert. An dieser Stelle sollte die eingegebene Kartennummer nicht weniger als 16 Ziffern und das eingegebene Passwort 4 Ziffern lang sein, sonst akzeptiert das System die Zahlung nicht. Nachdem der Kunde die Zahlung erfolgreich abgeschlossen hat, wird der Schreibtisch des Kunden geräumt und die Schuld auf 0 gesetzt. 5- Mit dieser Option wird das System abgemeldet. Wenn der Benutzer diese Option drückt, kommt er/sie wieder zum Passworteingabebildschirm. Wenn die Buchstaben "q“ oder "Q“ in einem der Benutzernamen- oder Passwortabschnitte auf dem Passworteingabebildschirm eingegeben werden, funktioniert der Code nicht mehr direkt.

