const Discord = require('discord.js');
const client = new Discord.Client();
 
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});
 
client.on('message', message => {
    if (message.content.includes('changeNick')) {
        client.setNickname({nick: message.content.replace('changeNick ', '')});
    }
});



client.login('DYyNzY4MzMwMDA1MjgyODE2.YIIm9g.UtXp2BLVpW52dHAke2crI0EY0l');