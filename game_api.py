#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request
import random

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/purchase_a_sword")
def purchase_a_sword():
    sword_name=random.choice(['Zulfiqar','Joyeuse','Masamune','Curved Saber of San Martin','Durendal','Seven Branched Sword','Legbiter','Excalibur'])
    sword_type={'Zulfiqar':'Double bladed sword','Joyeuse':'Medieval coronation sword','Masamune':'Japanese sword created by Masamune','Curved Saber of San Martin':'Curved saber',
            'Durendal':'Medievel one-handed straight sword','Seven Branched Sword':'Japanese ceremonial sword','Legbiter':'gaddhjat sword from Norway','Excalibur':'sword of King Arthur'}
    purchase_sword_event = {'event_type': 'purchase_sword','item_type':'sword','item_name':sword_name,'item_desc':sword_type[sword_name]}
    log_to_kafka('events', purchase_sword_event)
    return "Sword Purchased!\n"

@app.route("/join_guild")
def join_guild():
    guild_name=random.choice(['corpus naviculariorum','Freemen of the City','Basoche','Za','Masonry','Carpentry','Bakery'])
    guild_type={'corpus naviculariorum':'guild of long-distance shippers in Rome','Freemen of the City':'Medieval guild whose members had freedom from serfdom',
            'Basoche':'French guild of legal clerks','Za':'Trade guild of Japan','Masonry':'Masonry guild','Carpentry':'Organization of carpenters','Bakery':'Organization of bakers'}
    join_guild_event={'event_type':'join_guild','item_type':'guild','item_name':guild_name,'item_desc':guild_type[guild_name]}
    log_to_kafka('events',join_guild_event)
    return "You joined a guild!\n"

@app.route("/choose_nemesis")
def choose_nemesis():
    nemesis_name=random.choice(['Ursula','Darth Vader','Loki','Lord Voldemort','Norman Bates'])
    nemesis_type={'Ursula':'Tormentor of the little mermaid','Darth Vader':'villain and evil ruler of the Star Wars franchise',
            'Loki':'Agitator of the Marvel Universe','Lord Voldemort':'Evil mind of the Harry Potter world','Norman Bates':'Fictional serial killer, a total psycho'}
    choose_nemesis_event={'event_type':'choose_nemesis','item_type':'nemesis','item_name':nemesis_name,'item_desc':nemesis_type[nemesis_name]}
    log_to_kafka('events',choose_nemesis_event)
    return "You have a nemesis!\n"
    
