const Discord = require('discord.js');
const client = new Discord.Client();
client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    if (message.content.includes('changeNick')) {
        client.setNickname({nick: message.content.replace('changeNick ', 'dess')});
    }
});

client.login('NDYyNzY4MzMwMDA1MjgyODE2.X-_gkw.sj3Jsd2yqU8IX8jnsYPYvCQpCp4');
