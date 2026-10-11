<h1 align="center">Aut0iq</h1>

<p align="center">
  Делаю открытые приложения для своей музыки и домашнего сервера.<br>
  Всё крутится вокруг <a href="https://www.navidrome.org/">Navidrome</a>: скачать, разложить по жанрам, слушать.
</p>

<p align="center">
  <a href="https://github.com/Aut0iq?tab=repositories"><img src="https://img.shields.io/badge/проекты-открытый%20код-E6BD55?style=flat-square" alt="Открытый код"></a>
  <a href="https://www.navidrome.org/apps/"><img src="https://img.shields.io/badge/Navidrome-каталог%20приложений-7a2a45?style=flat-square" alt="Каталог приложений Navidrome"></a>
  <a href="https://aut0iq.qzz.io"><img src="https://img.shields.io/badge/сайт-aut0iq.qzz.io-3DDC84?style=flat-square" alt="aut0iq.qzz.io"></a>
</p>

---

## Музыка на своём сервере

Три проекта, которые работают вместе, но каждый полезен и сам по себе.

```
Coda  ──скачивает──▶  Navidrome  ──▶  Genre Mixes  ──собирает миксы──▶  Vici
```

### [Vici](https://github.com/Aut0iq/Vici) — плеер

<a href="https://github.com/Aut0iq/Vici/releases/latest"><img src="https://img.shields.io/github/v/release/Aut0iq/Vici?style=flat-square&color=E6BD55&label=release" alt="Релиз"></a>
<a href="https://github.com/Aut0iq/Vici/stargazers"><img src="https://img.shields.io/github/stars/Aut0iq/Vici?style=flat-square&color=E6BD55" alt="Звёзды"></a>
<img src="https://img.shields.io/badge/platform-Android%20%7C%20Windows%20%7C%20Linux-3DDC84?style=flat-square" alt="Android, Windows и Linux">

Музыкальный плеер для Navidrome и любого сервера с Subsonic API — на телефоне, на компьютере и в терминале. Есть в официальном [каталоге клиентов Navidrome](https://www.navidrome.org/apps/).

- **Интерфейс под обложку:** фон окрашивается в цвета играющего трека, панели полупрозрачные с настоящим размытием.
- **Визуализатор MilkDrop** на весь экран и тексты песен с построчной подсветкой.
- **Музыка без сети:** кэш альбомов или всей фонотеки, скробблинг Last.fm с очередью для офлайна.
- **Телефон:** виджет, настраиваемое нижнее меню, автозапуск при подключении наушников.

### [Coda](https://github.com/Aut0iq/Coda) — загрузчик

<a href="https://github.com/Aut0iq/Coda/releases/latest"><img src="https://img.shields.io/github/v/release/Aut0iq/Coda?style=flat-square&color=E6BD55&label=release" alt="Релиз"></a>
<img src="https://img.shields.io/badge/platform-Android-3DDC84?style=flat-square" alt="Android">

Приложение для Android, которое разворачивает ваш собственный сервер для скачивания музыки в Navidrome. Указываете адрес и логин Linux-сервера — приложение само подключается по SSH и ставит всё необходимое.

- **Установка с телефона,** без терминала: Docker, контейнеры и сертификат HTTPS.
- **Один сервер или два:** Navidrome может стоять рядом или на отдельной машине.
- **Аккуратные файлы:** точный подбор трека, теги и обложка, дубли и концертные версии пропускаются.
- **В паре с Vici:** поиск в плеере показывает и то, чего на сервере ещё нет, — добавляется одним нажатием.

### [Genre Mixes](https://github.com/Aut0iq/navidrome-genre-mixes) — миксы по жанрам

<a href="https://github.com/Aut0iq/navidrome-genre-mixes/releases/latest"><img src="https://img.shields.io/github/v/release/Aut0iq/navidrome-genre-mixes?style=flat-square&color=E6BD55&label=release" alt="Релиз"></a>
<a href="https://github.com/topics/navidrome-plugin"><img src="https://img.shields.io/badge/Navidrome-plugin-7a2a45?style=flat-square" alt="Плагин Navidrome"></a>

Плагин Navidrome, который держит по одному плейлисту на жанр — `Black Metal Mix`, `Glam Rock Mix` — и перемешивает их по расписанию.

- **Поровну между артистами:** исполнитель с 200 треками не вытесняет того, у кого их 20.
- **Один артист не идёт два раза подряд.**
- **Тегер жанров в комплекте:** дописывает в файлы поджанры с MusicBrainz.

## Другое

- **[vm-console-paste](https://github.com/Aut0iq/vm-console-paste)** — расширение для Firefox и Zen: вставляет текст из буфера обмена в веб-консоли виртуальных машин (Proxmox noVNC, xterm.js), «печатая» его нажатиями клавиш.
- **[aut0iq.qzz.io](https://aut0iq.qzz.io)** — мой сайт; его исходник лежит в [этом репозитории](https://github.com/Aut0iq/Aut0iq) (`index.html` со встроенными стилями и `checker.py`).

## Чем пользуюсь

<p>
  <img src="https://img.shields.io/badge/JavaScript-E6BD55?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/React%20Native-20232a?style=flat-square&logo=react" alt="React Native">
  <img src="https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo" alt="Expo">
  <img src="https://img.shields.io/badge/Electron-2b2e3a?style=flat-square&logo=electron" alt="Electron">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white" alt="Proxmox">
</p>

---

<p align="center">
  Нашли ошибку или есть идея — открывайте issue в нужном репозитории.
</p>
