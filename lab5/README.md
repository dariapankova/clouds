# Лабораторная 5

## Задания для лабораторной

#### Обычная:

Сделать мониторинг сервиса, поднятого в кубере (использовать, например, prometheus и grafana). Показать хотя бы два рабочих графика, которые будут отражать состояние системы. Приложить скриншоты всего процесса настройки.

## Выполнение лабораторной

### Обычная:

Для начала была прочитана невероятная [статья на хабре](https://habr.com/ru/companies/agima/articles/524654/), которая очень сильно помогла в выборе сервиса для мониторинга и в целом в установке. Автор супер крут.

С третьей лабы у нас сохранился кубер, поэтому обошлось без установки.

С помощью brew был установлен менеджер пакетов helm, через него уже был добавлен и установлен Prometheus. 

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace
```

Также с grafana:

```
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install grafana grafana/grafana --namespace monitoring
```

Первое, что мы сделали, это получили данные от grafana и смогли зайти в аккаунт. Очень сильно порадовались, что все получилось. Если бы мы знали...

```
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
kubectl port-forward --namespace monitoring svc/grafana 3000:80
```

(тут скрин графаны)

Дальше мы узнали имя пода и пробросили его на сервер с помощью следующих команд:

```
export POD_NAME=prometheus-server-644d686bc6-7lmg7
kubectl --namespace monitoring port-forward $POD_NAME 9090
```

По адресу http://127.0.0.1:9090/ находилось вот это:

(фотка прометеуса)

Мы изучили этот нехитрый интерфейс и ушли (в дебри) думать, какой же сервис нам мониторить. В итоге остановились на Редисе, как и в статье, хотя в установке она и не сильно нам помогла.

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```
Дальше создали пространство имен, чтобы понимать, где у нас в подах Редис.

```
kubectl create namespace redis
```
Дальше скачали Редис.

```
helm install redis bitnami/redis -n redis --set cluster.enabled=true --set cluster.slaveCount=2 --set master.persistence.enabled=false --set slave.persistence.enabled=false

```
После этого проверили, что все поды Редиса запущены.

```
kubectl get pod -n redis
```

Один из подов у нас не развернулся, мы глянули его логи:

```
kubectl logs redis-replicas-0 -n redis
```

Вообще можно еще почитать статус пода (мы дальше это несколько раз делали) ```kubectl describe pod redis-replicas-0 -n redis``` но на этот раз уже во время логов под подключился к мастеру и синхронизировался. Во время выполнения этой лабы мы познали простую истину: часто, чтобы что-то заработало, нужно немного подождать. И еще немного. И еще немного. Если уж совсем долго ждем, то можно и перезапустить. Под, кубер, докер, комп. А потом еще подождать.

В итоге поды заработали. Выглядели они как-то так:

(скрин подов)

Тут видно, что Редис был не первым нашим решением, сперва это был MySQL, который мы отчаялись починить и в итоге решили начать заново (это тоже, кстати, инсайт выполнения этой лабы).

После этого мы создали файл values.yaml, как в статье. Обновили Редис:

```
helm upgrade redis -f redis/values.yaml bitnami/redis -n redis
```

В общем-то, все заработало. Мы открыли Prometheus ранее описанным способом и смогли увидеть там данные о состоянии Редис. После этого вернулись в самое начало и открыли и grafana. Соорудили графики redis_connected_clients и redis_up, первый показывает количество подключенных клиентов, а второй - что Редис работает. Как видно, лабу мы делали долго.

()
