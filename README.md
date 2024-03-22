Projenin tek deposudur.
Paylaşmak yasak.Paylaşırsanız donunuza kadar alırım.
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

Destek için teşşekürler: [FortmanForever](https://github.com/FortmanForever)

# Techolay Social Raffle Script
It collects users who participate in a raffle on a specified subject and randomly selects a winner among these users.
# INSTALLATION AND USE
Download Python. Then install the modules.

Bash:
pip install requests

Bash:
pip install beautifulsoup4

Get the codes either from GitHub or here and save them as .py.
CTRL + Shift right Click open command window here (do this in Python file) "py filename.py"
Then enter the topic link, then the page number and done.
# MODULES USED.
requests module: to retrieve pages from the specified Topic.
Beautiful Soup module: to find user comments and usernames on the specified topic.
random module: to randomly select a winner from a list of usernames..

# WORKING LOGIC
get_usernames function: scans each page on the specified topic and returns "agree." It takes usernames from comments containing the phrase. It does not re-import previously selected users.
select_winner function: randomly selects a winner from a list of usernames.
main function: receives the URL and page number of the giveaway topic from the user. It retrieves the participating users using the get_usernames function, then prints those users to the screen and selects a winner using the select_winner function:.
NOTE: Just "I agree." It takes the statement, do not write anything else.

Thanks for the support: [FortmanForever](https://github.com/FortmanForever)
