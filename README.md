# Techolay Sosyal Çekiliş Script
Belirtilen bir konudaki çekiliş konusunda katılan kullanıcıları topluyor ve bu kullanıcılar arasından rastgele bir kazanan seçiyor.
# KURULUM VE KULLANIM
Python indirin. Sonra modülleri kurun.

Bash:
pip install requests

Bash:
pip install beautifulsoup4

İster GitHub'dan ister buradan kodları alın ve .py olarak kaydedin.
CTRL + Shift sağ Click komut penceresini burada aç (Python dosyasında yapın bunu) "py dosyaismi.py"
Sonra konu linki girin, sonra sayfa sayısını ve bitti.
# KULLANILAN MODÜLLER.
requests modülü: belirtilen Konu'dan sayfaları almak için.
Beautiful Soup modülü: belirtilen konuda kullanıcı yorumlarını ve kullanıcı adlarını bulmak için.
random modülü: kullanıcı adları listesinden rastgele bir kazanan seçmek için..

# ÇALIŞMA MANTIĞI
get_usernames fonksiyonu: belirtilen konudaki her bir sayfayı tarar ve "katılıyorum." ifadesini içeren yorumlardan kullanıcı adlarını alıyor. Daha önce seçilmiş kullanıcıları tekrar almaz.
select_winner fonksiyonu: kullanıcı adları listesinden rastgele bir kazanan seçiyor.
main fonksiyonu: kullanıcıdan çekiliş konusunun URL'sini ve sayfa sayısını alır. get_usernames fonksiyonunu kullanarak katılan kullanıcıları alır, ardından bu kullanıcıları ekrana yazdırır ve select_winner fonksiyonunu: kullanarak bir kazanan seçiyor.

NOT: Sadece "Katılıyorum." ifadesini alıyor başka birşey yazmayın.
