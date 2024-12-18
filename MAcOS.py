#GitHub: https://github.com/TakizawaXD/MAGBOT

import discord
from discord.ext import commands
import random
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="T", intents=intents)
Base = declarative_base()
class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    hugs = Column(Integer, default=0)  # Inicializa con 0
    kisses = Column(Integer, default=0)  # Inicializa con 0
    slaps = Column(Integer, default=0)  # Inicializa con 0
    pats = Column(Integer, default=0)  # Inicializa con 0
    highfives = Column(Integer, default=0)  # Inicializa con 0
    dominance = Column(Integer, default=0)  # Inicializa con 0
    money = Column(Integer, default=0)  # Inicializa con 0
    work_done = Column(Integer, default=0)  # Trabajos realizados

    def __repr__(self):
        return f"<UserProfile(user_id={self.user_id}, hugs={self.hugs}, kisses={self.kisses}, slaps={self.slaps}, pats={self.pats}, highfives={self.highfives}, dominance={self.dominance}, money={self.money}, work_done={self.work_done})>"

engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
@bot.command()
async def hug(ctx, user: discord.Member):
    user_profile = session.query(UserProfile).filter_by(user_id=user.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=user.id)
        session.add(user_profile)
    user_profile.hugs += 1
    session.commit()
    gifs = [
        "https://media.tenor.com/PMJdOBkmPUMAAAAM/hug-anime-kurome.gif",
        "https://media.tenor.com/BYH8Z_RhioYAAAAM/anya-forger-spy-x-family.gif",
        "https://media.tenor.com/59OfAXf4EUMAAAAM/anime-drawing.gif"
    ]
    await ctx.send(f"🤗 {ctx.author.mention} abrazó a {user.mention} ({user_profile.hugs} abrazos en total)!",
                   embed=discord.Embed().set_image(url=random.choice(gifs)))
@bot.command()
async def kiss(ctx, user: discord.Member):
    user_profile = session.query(UserProfile).filter_by(user_id=user.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=user.id)
        session.add(user_profile)

    user_profile.kisses += 1
    session.commit()

    gifs = [
        "https://media.tenor.com/Daj-Pn82PagAAAAM/gif-kiss.gif",
        "https://media.tenor.com/UcnfRWqnQtEAAAAM/kiss-anime-cute.gif",
        "https://media.tenor.com/F02Ep3b2jJgAAAAM/cute-kawai.gif",
        "https://media.tenor.com/xYUjLVz6rJoAAAAM/mhel.gif",
        "https://media.tenor.com/NZUQilMD3IIAAAAM/horimiya-izumi-miyamura.gif"
    ]
    await ctx.send(f"😘 {ctx.author.mention} besó a {user.mention} ({user_profile.kisses} besos en total)!",
                   embed=discord.Embed().set_image(url=random.choice(gifs)))
@bot.command()
async def slap(ctx, user: discord.Member):
    user_profile = session.query(UserProfile).filter_by(user_id=user.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=user.id)
        session.add(user_profile)

    user_profile.slaps += 1
    session.commit()
    gifs = [
        "https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif",
        "https://media.tenor.com/eU5H6GbVjrcAAAAM/slap-jjk.gif",
        "https://media.tenor.com/Sv8LQZAoQmgAAAAM/chainsaw-man-csm.gif",
        "https://media.tenor.com/WR_V0PKeUroAAAAM/hibi-slap.gif",
        "https://media.tenor.com/qsfk5t5qiqwAAAAM/angel-beats-yuri-nakamura.gif",
        "https://media.tenor.com/CAesvxP0KyEAAAAM/shinobu-kocho-giyuu-tomioka.gif"
    ]
    await ctx.send(f"👋 {ctx.author.mention} abofeteó a {user.mention} ({user_profile.slaps} bofetadas en total)!",
                   embed=discord.Embed().set_image(url=random.choice(gifs)))
@bot.command()
async def pat(ctx, user: discord.Member):
    user_profile = session.query(UserProfile).filter_by(user_id=user.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=user.id)
        session.add(user_profile)
        session.commit() 
    if user_profile.pats is None:
        user_profile.pats = 0  

    user_profile.pats += 1  
    session.commit()  
    gifs = [
        "https://media.tenor.com/fro6pl7src0AAAAM/hugtrip.gif",
        "https://media1.tenor.com/m/SLf-AWVC1VwAAAAC/cat-love-live.gif",
        "https://media.tenor.com/5lcF7ZEfNA0AAAAj/gawr-gura.gif",
        "https://media.tenor.com/J42otMNRBZ0AAAAM/pat.gif",
        "https://media.tenor.com/Tt8q-VRvMcsAAAAM/tohru-honda-ayame-soma.gif",
        "https://media.tenor.com/SRRnWa6nMAoAAAAM/foxplushy-foxy.gif",
        "https://media.tenor.com/YeJVoP3ri2cAAAAM/beast-tamer-anime-pat.gif"
    ]
    await ctx.send(f"🫶 {ctx.author.mention} acarició a {user.mention} ({user_profile.pats} caricias en total)!",
                   embed=discord.Embed().set_image(url=random.choice(gifs)))

@bot.command()
async def highfive(ctx, user: discord.Member):
    user_profile = session.query(UserProfile).filter_by(user_id=user.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=user.id)
        session.add(user_profile)

    user_profile.highfives += 1
    session.commit()

    gifs = [
        "https://media.tenor.com/ia0eAUSTgHAAAAAM/high-five-high5.gif",
        "https://media.tenor.com/7KVY_BxUWbEAAAAM/high-five-anime.gif",
        "https://media.tenor.com/RxLDEmFElGwAAAAM/no-game-no-life-ngnl.gif",
        "https://media.tenor.com/aqrmP6L_9wgAAAAM/love-live-win.gif",
        "https://media.tenor.com/ENGhNOukmSoAAAAM/vermeil-in-gold-alto-goldfield.gif"
    ]
    await ctx.send(f"✋ {ctx.author.mention} le dio un choca esos cinco a {user.mention} ({user_profile.highfives} choca esos cinco en total)!",
                   embed=discord.Embed().set_image(url=random.choice(gifs)))

@bot.command()
async def dom(ctx, user: discord.Member):
    user_profile = session.query(UserProfile).filter_by(user_id=user.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=user.id)
        session.add(user_profile)
    user_profile.dominance += 1
    session.commit()
    gifs = [
        "https://media1.tenor.com/m/pYZSJwJZNq4AAAAd/itadori-yuji.gif",
        "https://media.tenor.com/YD2DwvPE-DwAAAAM/sukuna-malevolent-shrine.gif",
        "https://media.tenor.com/0SDB9pQYY3IAAAAM/jujutsu-kaisen-shibuya-arc-mahito-shibuya-arc.gif",
        "https://media.tenor.com/HJlN95-e6IEAAAAM/gojo-vs-sukuna-cherry.gif",
        "https://media.tenor.com/KzfKU1opLb8AAAAM/satoru-gojo-gojo.gif"
    ]
    await ctx.send(f"👑 {ctx.author.mention} mostró su dominio sobre {user.mention} ({user_profile.dominance} dominios en total)!",
                   embed=discord.Embed().set_image(url=random.choice(gifs)))

@bot.command()
async def shop(ctx):
    embed = discord.Embed(title="Tienda de Trabajos", description="Aquí puedes ver los trabajos disponibles.", color=discord.Color.green())
    embed.add_field(name="Trabajo 1: Recolectar piedras", value="Ganas 50 monedas", inline=False)
    embed.add_field(name="Trabajo 2: Reparar el sistema", value="Ganas 100 monedas", inline=False)
    embed.add_field(name="Trabajo 3: Limpiar el servidor", value="Ganas 30 monedas", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def work(ctx, job: str):
    user_profile = session.query(UserProfile).filter_by(user_id=ctx.author.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=ctx.author.id)
        session.add(user_profile)
    if job == "1":
        user_profile.money += 50
        user_profile.work_done += 1
        session.commit()
        await ctx.send(f"{ctx.author.mention} completó el trabajo de Recolectar piedras y ganó 50 monedas!")
    elif job == "2":
        user_profile.money += 100
        user_profile.work_done += 1
        session.commit()
        await ctx.send(f"{ctx.author.mention} completó el trabajo de Reparar el sistema y ganó 100 monedas!")
    elif job == "3":
        user_profile.money += 30
        user_profile.work_done += 1
        session.commit()
        await ctx.send(f"{ctx.author.mention} completó el trabajo de Limpiar el servidor y ganó 30 monedas!")
@bot.command()
async def balance(ctx):
    user_profile = session.query(UserProfile).filter_by(user_id=ctx.author.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=ctx.author.id)
        session.add(user_profile)
        session.commit()
    await ctx.send(f"{ctx.author.mention} tiene {user_profile.money} monedas y ha completado {user_profile.work_done} trabajos.")
@bot.command()
async def stats(ctx):
    user_profile = session.query(UserProfile).filter_by(user_id=ctx.author.id).first()
    if not user_profile:
        user_profile = UserProfile(user_id=ctx.author.id)
        session.add(user_profile)
        session.commit()
    await ctx.send(f"Estadísticas de {ctx.author.mention}:"
                   f"\nAbrazos: {user_profile.hugs}"
                   f"\nBesos: {user_profile.kisses}"
                   f"\nBofetadas: {user_profile.slaps}"
                   f"\nCaricias: {user_profile.pats}"
                   f"\nChoca esos cinco: {user_profile.highfives}"
                   f"\nDominio: {user_profile.dominance}"
                   f"\nMonedas: {user_profile.money}"
                   f"\nTrabajos completados: {user_profile.work_done}")

bot.run('REPLACE_WITH_YOUR_DISCORD_TOKEN')