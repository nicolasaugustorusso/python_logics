import lightbulb

#para iniciar o Bot;
#token = token do bot | 'r').read() = modo de leitura para arquivos .txt
#default_enable_guilds = por ser lido como string, passamos para int(). id do servidor
bot = lightbulb.BotApp(token=open('tokens/token_ds.txt', 'r').read(), default_enabled_guilds=(int(open('tokens/ds_channel_id.txt', 'r').read())))

@bot.command
@lightbulb.command('msg_asmv', 'Saudação Bot do Russo')
#.SlashCommand = diz que a barra será lida como comando (slash = barra in english)
@lightbulb.implements(lightbulb.SlashCommand)
#criada uma função asyncrôna, com o parâmentro de contextualização(identifica 
# o que está dentro do nosso comando quando executado)
#await ctx.respond = método de resposta
async def hello(ctx):
    await ctx.respond('*Olá, aqui é o bot do Russo!*')

#Calculadora
@bot.command
@lightbulb.command('calculadora','Calculadora')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_calculator(ctx):
    pass

@my_calculator.child
@lightbulb.option('n2', 'segundo número', type=float)
@lightbulb.option('n1', 'primeiro número', type=float)
@lightbulb.command('soma', 'Operação de Adição')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    r = ctx.options.n1 + ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

#Temperatura com API
import requests
import string

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('tokens/api_weather_key.txt', 'r').read()

def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

@bot.command
@lightbulb.option('pais', 'País', type=str)
@lightbulb.option('cidade', 'Cidade', type=str)
@lightbulb.command('temperatura', 'Informe uma cidade e seu país para saber as condições climáticas atuais')
@lightbulb.implements(lightbulb.SlashCommand)

async def temperatura(ctx):
    country = ctx.options.pais
    CITY = string.capwords(ctx.options.cidade) + "," + country[0:2].lower()
    url = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    umidade = response['main']['humidity']
    vento = response['wind']['speed']

    temp_celcius = str(round(kelvin_to_celcius(temp_kelvin)))

    await ctx.respond(f'```A temperatura atual em {string.capwords(ctx.options.cidade)} é de {temp_celcius} °C \nUmidade do ar: {umidade}% \nVento: {vento}m/s```')

bot.run()