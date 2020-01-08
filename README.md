# prom_pi_temp.py: expose Raspberry Pi temperatures to Prometheus

This little script grabs Raspberry Pi CPU and GPU temperatures and stores them in a text file formatted for [node_exporter](https://github.com/prometheus/node_exporter), where Prometheus can scrape them.


### Usage
1. Install node_exporter and enable the [textfile collector](https://github.com/prometheus/node_exporter#textfile-collector).
1. Install `prom_pi_temp.py`.
1. Setup a cron job to run `prom_pi_temp.py` and save the output to a text file in the directory you configured above.
1. Confirm you can see the temperature metrics.


```shell
node_exporter --collector.textfile.directory=/var/run/node_exporter_textfile
echo '* * * * * /usr/local/bin/prom_pi_temp.py > /var/run/node_exporter_textfiles/temps.prom' > /etc/cron.d/prom_pi_temp.cron
curl -s localhost:9100/metrics | grep node_temp
```

Improvements welcome!!
