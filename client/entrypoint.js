#!/usr/bin/env node

const childProcess = require('child_process');

const DEBUG = process.env.DEBUG === 'true';

// Запуск приложения

let appProcess = null;

appProcess = childProcess.spawn('npm', ['install']);
if(DEBUG){
    appProcess = childProcess.spawn('npm', ['run', 'host']);
}
else{
    appProcess = childProcess.spawn('npm', ['run', 'build']);
}

// Проброс вывода из дочернего процесса в стандартный вывод контейнера Docker
appProcess.stdout.pipe(process.stdout);
appProcess.stderr.pipe(process.stderr);

// Обработка сигналов завершения для корректного завершения приложения и контейнера
process.on('SIGINT', () => {
  appProcess.kill('SIGINT');
  process.exit(0);
});

process.on('SIGTERM', () => {
  appProcess.kill('SIGTERM');
  process.exit(0);
});