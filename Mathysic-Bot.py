import discord
from discord.ext import commands
import itertools
import time

pi = 22/7

bot = commands.Bot("m/")



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Mathysic - Math and Physics assistant."))
    print("Ready.")

@bot.command()
async def helps(ctx):

    embed = discord.Embed(
        title = "Help",
        description = "Hi!",
        colour = discord.Colour.green()
    )
    embed.set_footer(text="How can i help you?")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891932198268207149/891936937798144020/einstein.png")
    embed.set_author(name="Mathysic")
    embed.add_field(name="Information",value="Hi guys! I'm a math and also a physics bot. I was programmed to help you with your homework!\nAs for the little information, you will have to comply with some things to use me!\nPlease don't enter another unit from 'cm' on lengths in physics, and If you can't get a response from the command you entered, make sure you typed it correctly.")
    await ctx.send(embed=embed)

@bot.command()
async def menu(ctx):

    embed = discord.Embed(
        title = "Menu",
        description = "Hi!",
        colour = discord.Colour.green()
    )
    embed.set_footer(text="How can i help you?")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891932198268207149/891936937798144020/einstein.png")
    embed.set_author(name="Mathysic")
    embed.add_field(name="Calculator", value="You can run the calculator by typing m/calc.")
    embed.add_field(name="Math", value="You can run the math commands by typing m/math.")
    embed.add_field(name="Physic", value="You can run the physic commands by typing m/phys.")
    await ctx.send(embed=embed)

@bot.command()
async def math(ctx):
    embed = discord.Embed(
        title = "Mathematic Help",
        description = "Hi!",
        colour = discord.Colour.red()
    )
    embed.set_footer(text="How can i help you?")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891932198268207149/891936937798144020/einstein.png")
    embed.set_author(name="Mathysic \n------------------------------------------------------------------")
    embed.add_field(name="Permitation", value="You can permitation numbers by typing m/perm <a> <b> <c>.")
    embed.add_field(name="Combination", value="You can combination numbers by typing m/comb <a> <b> <c>.")
    embed.add_field(name="GCD", value="You can find the gcd of numbers by typing m/gcd <a>.")
    embed.add_field(name="LCM", value="You can find the lcm of numbers by typing m/lcm <a>.")
    embed.add_field(name="Factorial", value="You can find the factorial of numbers by typing m/fac <a>.")
    embed.add_field(name="Pythagoras Theorem", value="You can find the pythagoras theorem of numbers by typing m/pytheorem <a> <b>.")
    embed.add_field(name="Length Converter", value="You can convert length by typing m/lconvert <a> <length> <length2>.")
    embed.add_field(name="Square Root", value="You can square root numbers by typing m/sqroot <a>")
    embed.add_field(name="Area Calculations", value="You can calculate area by typing m/area")
    embed.add_field(name="Exponential Calculations", value="You can calculate exponential calculations by typing m/excal <number1> <number2> .")
    await ctx.send(embed=embed)

@bot.command()
async def area(ctx):
    embed = discord.Embed(
        title = "Area Help",
        description = "Hi!",
        colour = discord.Colour.red()
    )
    embed.set_footer(text="How can i help you?")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891932198268207149/891936937798144020/einstein.png")
    embed.set_author(name="Mathysic")
    embed.add_field(name="Circle Area", value="You can calculate circle area by typing m/circ <radius>.")
    embed.add_field(name="Square Area", value="You can calculate square area by typing m/squ <side1 cm> <side2 cm>.")
    embed.add_field(name="Triangle Area", value="You can calculate triangle area by typing m/tria <side1 cm> <side2 cm> <side3 cm>.")
    embed.add_field(name="Rectangle Area", value="You can calculate rectangle area by typing m/rect <length cm> <breadth cm>.")
    await ctx.send(embed=embed)

@bot.command()
async def circ(ctx,a:float):
    calc = pi*a**2
    await ctx.send(f"Area is {calc} cm")

@bot.command()
async def squ(ctx,a:float,b:float):
    calc = a*b
    await ctx.send(f"Area is {calc} cm")

@bot.command()
async def tria(ctx,a:float,b:float,c:float):
    d = (a + b + c) / 2
    calc = (d*(d-a)*(d-b)*(d-c)) ** 0.5
    await ctx.send(f"Area is {calc} cm")

@bot.command()
async def rect(ctx,a:float,b:float):
    calc = a*b
    await ctx.send(f"Area is {calc} cm")

@bot.command()
async def sqroot(ctx,a:float):
    calc = a**(1/2)
    await ctx.send(f"{a} Square root is {calc}")

@bot.command()
async def lconvert(ctx,a:float,b:str,c:str):
    if b == "mm" and c == "cm":
        ans = a / 10
        await ctx.send(f"{a} mm = {ans} cm")
    elif b == "mm" and c == "m":
        ans = a / 1000
        await ctx.send(f"{a} mm = {ans} m")
    elif b == "mm" and c == "km":
        ans = a / 1000000
        await ctx.send(f"{a} mm = {ans} km")
    elif b == "cm" and c == "mm":
        ans = a * 10
        await ctx.send(f"{a} cm = {ans} mm")
    elif b == "cm" and c == "m":
        ans = a / 100
        await ctx.send(f"{a} cm = {ans} m")
    elif b == "cm" and c == "km":
        ans = a / 100000
        await ctx.send(f"{a} cm = {ans} km")
    elif b == "m" and c == "mm":
        ans = a * 1000
        await ctx.send(f"{a} m = {ans} mm")
    elif b == "m" and c == "cm":
        ans = a * 100
        await ctx.send(f"{a} m = {ans} cm")
    elif b == "m" and c == "km":
        ans = a / 1000
        await ctx.send(f"{a} m = {ans} km")
    elif b == "km" and c == "mm":
        ans = a * 1000000
        await ctx.send(f"{a} km = {ans} mm")
    elif b == "km" and c == "cm":
        ans = a * 100000
        await ctx.send(f"{a} km = {ans} cm")
    elif b == "km" and c == "m":
        ans = a * 1000
        await ctx.send(f"{a} km = {ans} m")

@bot.command()
async def pytheorem(ctx,a:float,b:float):
    total = a ** 2 + b ** 2
    hypotenuse = total ** 0.5
    await ctx.send(f"Hypotenuse is {hypotenuse}")

@bot.command()
async def fac(ctx,b:int):
    a = 1
    for i in range(1, b + 1):
        a = a * i
    await ctx.send(f"{b} Factorial is {a}")

@bot.command()
async def perm(ctx,a:str,b:str,c:str):
    await ctx.send(f"```{a}, {b} and {c} Permitation is...```")
    time.sleep(5)
    for permitation in itertools.permutations([a,b,c]):
        await ctx.send(permitation)
    
@bot.command()
async def comb(ctx,a:str,b:str,c:str):
    await ctx.send(f"```{a}, {b} and {c} Permitation is...```")
    time.sleep(5)
    for combination in itertools.combinations([a,b,c], 2):
        await ctx.send(combination)

@bot.command()
async def gcd(ctx,a:int,b:int):
    answer = min(a, b)
    GCD = 1

    for i in range(1, answer + 1):
        if a % i == 0 and b % i == 0:
            GCD = i
    
    await ctx.send(f"{a} and {b} gcd is {GCD}")

@bot.command()
async def lcm(ctx,a:int,b:int):
    LCM = a * b
    for number in range(LCM, max(a, b) - 1, -1):
        if number % a == 0 and number % b == 0:
            LCM = number
    
    await ctx.send(f"{a} and {b} lcm is {LCM}")

@bot.command()
async def calc(ctx):

    embed = discord.Embed(
        title = "Calculator Help",
        description = "Hi!",
        colour = discord.Colour.red()
    )
    embed.set_footer(text="How can i help you?")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891932198268207149/891936937798144020/einstein.png")
    embed.set_author(name="Mathysic")
    embed.add_field(name="Add", value="You can add numbers by typing m/add <a> <b>.")
    embed.add_field(name="Sub", value="You can sub numbers by typing m/sub <a> <b>.")
    embed.add_field(name="Multiply", value="You can multiple numbers by typing m/multiply <a> <b>.")
    embed.add_field(name="Divide", value="You can divide numbers by typing m/divide <a> <b>.")
    await ctx.send(embed=embed)

@bot.command() 
async def add(ctx,a:float,b:float): 
    await ctx.send(f"{a} + {b} = {a+b}")

@bot.command() 
async def sub(ctx,a:float,b:float): 
    await ctx.send(f"{a} - {b} = {a-b}")

@bot.command() 
async def multiply(ctx,a:float,b:float): 
    await ctx.send(f"{a} * {b} = {a*b}")

@bot.command() 
async def divide(ctx,a:float,b:float): 
    await ctx.send(f"{a} / {b} = {a/b}")

@bot.command()
async def physic(ctx):
    embed = discord.Embed(
    title = "Physic Help",
    description = "Hi!",
    colour = discord.Colour.red()
    )
    embed.set_footer(text="How can i help you?")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891932198268207149/891936937798144020/einstein.png")
    embed.set_author(name="Mathysic \n------------------------------------------------------------------")
    embed.add_field(name="Volume calculation",          value="You can reach volume calculations by typing m/volcalcs.")
    embed.add_field(name="Temperature Converter", value="You can calculate the heat conversions by typing m/tconvert <a> <C/K/F> <C/K/F>.")
    embed.add_field(name="Mass Calculations", value="You can make mass calculations by typing  m/mass <a> <unit1> <unit2>.")
    embed.add_field(name="Pressure Calculations ", value="You can make  pressure calculations by typing  m/prsure <force> <field>.")
    embed.add_field(name="Power Calculations", value= "You can make power calculations by typing  m/powr <work-done-value> <time(in seconds)>.")
    embed.add_field(name="Energy Calculations", value= "You can make Energy Calculations by typing  m/energy.")    
    await ctx.send(embed=embed)

@bot.command()
async def powr(ctx,a:float,b:float):
    calc = a/b
    await ctx.send(f"Result: {calc}")

@bot.command()
async def energy(ctx):
    embed = discord.Embed(
        title = "Energy Help",
        description = "Hi!",
        colour = discord.Colour.red()
    )
    embed.set_footer(text="How can i help you?")
    embed.set_author(name="Mathysic \n------------------------------------------------------------------")
    embed.add_field(name="Kinetic Energy Calculations", value="You can calculate kinetic energy by typing m/kinetic <mass of matter(kg)> <velocity of matter(km/s)>.")
    embed.add_field(name="Potential Energy Calculations", value="You can calculate potential energy by typing m/potent <mass of matter(kg)> <gravitational acceleration(m/s²)> <height(m)>.")

@bot.command()
async def kinetic(ctx,a:float,b:float):
    calc = a*b*1/2
    await ctx.send(f"Result: {calc}")

@bot.command()
async def potent(ctx,a:float,b:float,c:float):
    calc = a*b*c
    await ctx.send(f"Result: {calc}")

@bot.command()
async def prsure(ctx,a:float,b:float):
    calc = a/b
    await ctx.send(f"Result: {calc}")


@bot.command()
async def mass(ctx,num1:float,unit1:str,unit2:str):
    if unit1== 'Kg' and unit2== 'G':
        await ctx.send(f'{num1} Kg = {num1/0.0010000} g')
    elif unit1== 'Kg' and unit2== 'Mg':
        await ctx.send(f'{num1} Kg = {num1*1000000} Mg')
    elif unit1== 'Kg' and unit2== 'T':
        await ctx.send(f'{num1} Kg = {num1/1000} T')

    elif unit1== 'G' and unit2== 'Kg':
        await ctx.send(f'{num1} g = {num1/1000} Kg')
    elif unit1== 'G' and unit2== 'Mg':
        await ctx.send(f'{num1} g = {num1*1000} Mg')
    elif unit1== 'G' and unit2== 'T':
        await ctx.send(f'{num1} g = {num1/1000000 } T') 

    elif unit1== 'Mg' and unit2== 'Kg':
        await ctx.send(f'{num1} Mg = {num1/1000000} Kg')
    elif unit1== 'Mg' and unit2== 'G':
        await ctx.send(f'{num1} Mg = {num1/1000 } G')
    elif unit1== 'Mg' and unit2== 'T':
        await ctx.send(f'{num1} Mg = {num1/1000000000 } T')

    elif unit1== 'T' and unit2== 'Kg':
        await ctx.send(f'{num1} T = {num1*1000} Kg')
    elif unit1== 'T' and unit2== 'G':
        await ctx.send(f'{num1} T = {num1*1000000 } G')
    elif unit1== 'T' and unit2== 'Mg':
        await ctx.send(f'{num1} T = {num1*1000000000 } Mg') 

@bot.command()
async def excal(ctx,a:float,b:float):
    calc = a**b
    await ctx.send(f"Result: {calc}")

@bot.command()
async def tconvert(ctx,a:float,unit1:str,unit2:str):
    if unit1 == 'C' and unit2== 'K':
        await ctx.send(f'{a} °C = {a+273.15} °K')
    elif unit1 == 'C' and unit2== 'F':
        await ctx.send(f'{a} °C = {a*9/5+32} °F')
    elif unit1== 'K' and unit2== 'C':
        await ctx.send(f'{a} °K = {a-273.15} °C')
    elif unit1== 'K' and unit2== 'F':
        await ctx.send(f'{a} °K = {a*9/5-459.67} °F')     
    elif unit1 =='F' and unit2== 'C':
        await ctx.send(f'{a} °F = {(a-32)*5/9} °C')
    elif unit1 =='F' and unit2== 'K':
        await ctx.send(f'{a} °F = {(a-32)/1.8000+273.15} °K')

@bot.command()
async def volcalcs(ctx):
    embed = discord.Embed(
        title = "Volume Help",
        description = "Hi!",
        colour = discord.Colour.red()
    )
    embed.set_footer(text="How can i help you?")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891932198268207149/891936937798144020/einstein.png")
    embed.set_author(name="Mathysic \n------------------------------------------------------------------")
    embed.add_field(name="Cube Volume", value="You can calculate cube volume by typing m/cube <edgesize>.")
    embed.add_field(name="Sphere Volume", value="You can calculate sphere volume by typing m/sph <radius>.")
    embed.add_field(name="Clynder Volume", value="You can calculate clynder volume by typing m/cly <height> <radius> .")
    embed.add_field(name="Triangular Prism Volume", value="You can calculate triangular prism volume by typing m/triang <base-side> <height>.")
    embed.add_field(name="Rectangular Prism Volume", value="You can calculate rectangular prism volume  by typing m/rectang <sole-edge1> <sole-edge2> <height>.")
    await ctx.send(embed=embed)

@bot.command()
async def cube(ctx,a:float):
    calc = a**3
    await ctx.send(f"Cube volume is {calc}")

@bot.command()
async def sph(ctx,a:float):
    calc = (4 / 3) * (pi * a ** 3)
    await ctx.send(f"Sphere volume is {calc}")

@bot.command()
async def cly(ctx,a:float,b:float):
    calc = pi * a ** 2 * b
    await ctx.send(f"Clynder volume is {calc}")

@bot.command()
async def triang(ctx,a:float,b:float):
    calc = a**2*b
    await ctx.send(f"Triangular Prism volume is {calc}")

@bot.command()
async def rectang(ctx,a:float,b:float,c:float):
    calc = a*b*c
    await ctx.send(f"Rectangular Prism volume is {calc}")

