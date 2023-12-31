# %%
import discord
from datetime import datetime, timedelta

TOKEN = None
file_path = "TOKEN.txt"

# Read TOKEN New
with open(file_path, 'r', encoding="UTF-8") as f: 
    TOKEN = f.read()
f.close()

# Picture Directory
pict_dir = {
    # 오리지날 로아콘
    "[뀨": "image/ku.png",
    "[눈물팡": "image/sosaaaadd.png",
    "[놀자에요": "image/playtogeth.png",
    "[놀자에몽": "image/playmong.png",
    "[두렵다": "image/afraid.png",
    "[모무룩": "image/saaddd.png",
    "[멘탈": "image/mental.png",
    "[못참지": "image/cannot.png",
    "[멈춰": "image/stop.png",
    "[문열어": "image/openthedoor.png",
    "[물음표": "image/whaaat.png",
    "[물끄럼": "image/lookstraight.png",
    "[방긋": "image/banguht.png",
    "[빛": "image/light.png",
    "[빠직": "image/bazik.png",
    "[신나": "image/happpy.png",
    "[슬퍼": "image/sad.png",
    "[안줘": "image/nogive.png",
    "[영차": "image/cheerup.png",
    "[웃기구요": "image/sofunny.png",
    "[웃프네요": "image/funbutnotfun.png",
    "[추천": "image/suggestion.png",
    "[멋쩍": "image/museok2.png",
    "[뭐라고요": "image/whatyousay.png",
    "[이이잉": "image/yiiiing.png",
    "[정말이요": "image/really.png",
    "[줘": "image/giveme.png",
    "[머쓱": "image/museok2.png",
    "[좋아요": "image/good.png",
    "[죽은척": "image/notdeath.png",
    "[짝짝": "image/clapclap.png",
    "[침묵": "image/nocomment.png",
    "[ㅋㅋㅋ": "image/zzz.png",
    "[호에엥": "image/wooow.png",
    "[핥짝": "image/hehheh.png",
    "[헤헷": "image/hahat.png",
    "[히죽": "image/smile.png",
    
    # 냥바타콘
    "[냥웃음": "image_cat/cat_smile.png",
    "[냥짱": "image_cat/cat_zzang.png",
    "[냥녹음": "image_cat/cat_meltdown.png",
    "[냥좌절": "image_cat/cat_discouragement.png",
    "[냥힘내": "image_cat/cat_cheerup.png",
    "[냥부끄": "image_cat/cat_shy.png",
    "[냥냥펀치": "image_cat/cat_punch.png",
    "[냥브이": "image_cat/cat_V.png",
    "[냥죽은척": "image_cat/cat_notdeath.png",
    "[냥으음": "image_cat/cat_ummmm.png",
    "[냥도로롱": "image_cat/cat_dororong.png",
    "[냐앗호": "image_cat/cat_yeah.png",
    "[냥허그": "image_cat/cat_hearthug.png",
    "[냥츄릅": "image_cat/cat_heee.png",
    "[냥행복": "image_cat/cat_happy.png",
    "[냥멈춰": "image_cat/cat_stopbadthing.png",
    "[냥치킨": "image_cat/cat_chicken.png",
    "[냥슬퍼": "image_cat/cat_sad.png",
    "[냥치킨": "image_cat/cat_chicken.png",
    "[냥다닥": "image_cat/cat_run.png",
    "[부끄럽냥": "image_cat/cat_shyee.png",
    "[냥ㅋㅋ": "image_cat/cat_haha.png",
    "[냐아아": "image_cat/cat_haaaappppyy.png",
    "[냐호": "image_cat/cat_yahoo.png",
    "[냥배부름": "image_cat/cat_full.png",
    # "[냥해탈": "image_cat/cat_hetal.png", # 이미지랑 안맞음
    "[냥냠냠": "image_cat/cat_yumyum.png",
    "[냥냥": "image_cat/cat_meow.png",
    "[냥먼산": "image_cat/cat_farmountain.png",
    "[냥쭈압": "image_cat/cat_yummycat.png",
    "[냥꾹": "image_cat/cat_push.png",
    "[쭈아압": "image_cat/cat_sqeeeze.png",
    "[찰떡냥": "image_cat/cat_chaltuk.png",
    
    # 응애 모코콩
    "[감사콩": "image_kong/thankyou.png",
    "[꺼억콩": "image_kong/fullkong.png",
    "[냠냠콩": "image_kong/nyamyanmkong.png",
    "[노래콩": "image_kong/songkong.png",
    "[더줘콩": "image_kong/givememorekong.png",
    "[도망콩": "image_kong/runkong.png",
    "[물줘콩": "image_kong/waterme.png",
    "[뿅콩": "image_kong/ppongkong.png",
    "[씨익콩": "image_kong/zkong.png",
    "[잘자콩": "image_kong/goodnightkong.png",
    "[촉촉콩": "image_kong/sadkong.png",
    "[츄릅콩": "image_kong/yummykong.png",

    # Special Edition
    "[강선부릅": "image_se/kangsun_1.jpg",
    "[속이뻥": "image_se/insideOUT.png",
    "[우에엥": "image_se/saduaeng.jpg",
    "[뿌엥": "image_se/buaeng.jpg",
    "[카멘슈슉": "image_se/kamenshushuk.png",
    "[카멘음": "image_se/kamenummm.png",
}

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # Change Bot State
        await self.change_presence(
            status=discord.Status.online, 
            activity=discord.Game("로아콘 준비")
        )
    
    # on Message imcoming
    async def on_message(self, message):
        def send_log(picture, time, user, channel, guild):
            # 기록용 파일 열기
            log_file_path = "LogFile.txt"
            log_f = open(log_file_path, 'a', encoding="UTF-8")
            
            time = time + timedelta(hours=9)
            time = time.strftime("%Y-%m-%d %H:%M:%S")
            log_f.write(f"\n{user}//{time} //>> Sent Command //{picture} at //{guild} //{channel}")
            log_f.close()
        
        trim_text = message.content.replace(" ", "")
        
        if message.author == self.user:
            return

        # 도움말
        elif (message.content == "[로아콘도움"):
            # Bring All Commands
            all_commands = []
            result = "" # Output Text
            for key in pict_dir.keys():
                all_commands.append(str(f"{key}"))
            all_commands.sort() # Sorting
            for key in all_commands:
                result += str(f"{key}")
                if (all_commands[-1]) != key: 
                    result += str(f", ")
            result = f"사용 가능한 명령어: {len(all_commands)}개\n{result}"
            # Create Discord Embed
            embed=discord.Embed(
                title="봇 명령어 모음 (스프레드시트)", 
                url="https://docs.google.com/spreadsheets/...", 
                description="""
                봇 명령어 검색 및 기타 자세한 내용은 상단 링크 참조  
                - 현재 비공개 알파 테스트 버전입니다.
                * 요청량이 많다면 일부 기능이 불안정 할 수 있습니다.  
                
                > **버그 제보**는 id "비공개" 한테 DM 주세용
                > 건의사항, 개선점, 피드백 환영합니다!!!!
                """, 
                color=0x00ff56
            )
            image = discord.File("image/playtogeth.png", filename="image.png")
            embed.set_thumbnail(url='attachment://image.png')
            embed.add_field(name="명령어에 대한 지원이 도착했습니다!", value=result, inline=True)
            await message.channel.send(embed=embed, file=image)
            await message.delete()
            send_log(trim_text, message.created_at, message.author, message.channel, message.guild)
        
        # 이스터에그
        elif (message.content == '[이스터에그'):
            await message.channel.send(f'이스터에그를 발견하셨군요! 하지만 별거 없다능\n(버전업 되면 뭔가 생길수도...)')
            send_log(trim_text, message.created_at, message.author, message.channel, message.guild)
        
        # 비어있는 문자이면
        # elif (trim_text == '' or None): return
        
        # 이모티콘 출력
        elif (trim_text in pict_dir.keys()): 
            image = discord.File(pict_dir[trim_text], filename="image.png")
            embed = discord.Embed()
            embed.set_image(url='attachment://image.png')
            await message.channel.send(embed=embed, file=image)
            await message.delete()
            send_log(trim_text, message.created_at, message.author, message.channel, message.guild)
            
        else: return

# Execute Discord Bot
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
