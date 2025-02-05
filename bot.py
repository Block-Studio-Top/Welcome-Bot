import discord
import json

# 讀取 TOKEN
with open("TOKEN.txt", "r") as f:
    TOKEN = f.read().strip()

# 啟用 Intents 以監聽成員變動
intents = discord.Intents.default()
intents.members = True  # 允許監聽成員加入/離開
client = discord.Client(intents=intents)

# 讀取設定檔
def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

config = load_config()

# 當機器人成功啟動時
@client.event
async def on_ready():
    print(f"機器人已登入為 {client.user}")

# 當成員加入伺服器
@client.event
async def on_member_join(member):
    channel = client.get_channel(config["welcome_channel_id"])
    if channel:
        embed = discord.Embed(
            title="🎉 歡迎來到白雲生存服 😃👍",
            description=f"歡迎 {member.mention} 來到白雲生存服 😃\n\n"
                        f"快來看看伺服器規範 ⬇️\n"
                        f"🔹 <#{config['rules_channel_id']}>\n\n"
                        f"快來看看伺服器資訊 ⬇️\n"
                        f"📖 <#{config['info_channel_id']}>",
            color=0x00FF00
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else config["default_avatar"])
        await channel.send(embed=embed)

# 當成員離開伺服器
@client.event
async def on_member_remove(member):
    channel = client.get_channel(config["goodbye_channel_id"])
    if channel:
        embed = discord.Embed(
            title="👋 再見！",
            description=f"{member.mention} 歡迎再度光臨 **WhiteCloud | 白雲生存服** 😢\n有緣再會...",
            color=0xFF0000
        )
        embed.set_thumbnail(url=config["goodbye_image"])
        await channel.send(embed=embed)

# 啟動機器人
client.run(TOKEN)
