const RPC = require('discord-rpc');
const express = require('express');

const app = express();

const client = new RPC.Client({
    transport: 'ipc'
});

client.on('ready', () => {
    client.request('SET_ACTIVITY', {
        pid: process.pid,
        activity: {
            details: "Details Here",
            state: "State Here",
            timestamps: {
                start: Date.now()
            },
            assets: {
                large_image: "foto2", // large image key from developer portal > rich presence > art assets
                large_text: "large image text"
            },
            buttons: [
                { label: "Venha conhecer velinhas", url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO" },
                { label: "Click here", url: "https://www.youtube.com/watch?v=V2XcYkq9LxI" }
            ]
        }
    });
});

client.login({
    clientId: '781163638434168852', // put the client id from the dev portal here
    clientSecret: '' // put the client secret from the dev portal here
});
