##Linerate
Simple script to calculate an edge above which linerate is possible.

_Please, consider this information not as a proven research, but as a try one did to get the approximate 
state of current generation of merchant silicon._

The numbers outcome is a pure math which, as we know, might not (and surely don't) intersect with the real world.

Still have no idea how in report at link 2 (see below), the line rate for Broadcom Trident II (BCM56850) is above 84 bytes
packet size, but the script result is 227.

In opposite, the Juniper's presentation of QFX5200 applies that line rate for Broadcom Tomahawk (BCM56960) is possible with packet size
above 250, but the script result is 186.

The search continues ... *an UFO image*

###Output
```
[   Trident II BCM56850   ] 2560 Gbps / 1440  Mpps | Linerate if packet size is higher than 222
[  Trident II+ BCM56864   ] 2560 Gbps / 1000  Mpps | Linerate if packet size is higher than 320
[     Helix4 BCM56340     ] 256  Gbps /  191  Mpps | Linerate if packet size is higher than 167
[     Helix4 BCM56342     ] 208  Gbps /  156  Mpps | Linerate if packet size is higher than 166
[    Trident+ BCM56846    ] 1280 Gbps /  960  Mpps | Linerate if packet size is higher than 166
[    Tomahawk BCM56960    ] 6400 Gbps / 4400  Mpps | Linerate if packet size is higher than 181
[   Trident II BCM56854   ] 1440 Gbps / 1000  Mpps | Linerate if packet size is higher than 180
```

###Links

1. [Broadcom Strata XGS Family table](http://sk1f3r.ru/pic/broadcom-strata-xgs.png)
2. [Mellanox SX-2 vs Broadcom Trident II Performance Evaluation](https://www.mellanox.com/related-docs/products/Tolly-215111-Mellanox-SwitchX-2_Performance.pdf)
3. [Mellanox Spectrum vs Broadcom Tomahawk Performance Evaluation](http://www.mellanox.com/related-docs/products/tolly-report-performance-evaluation-2016-march.pdf)
4. [Buffer information for particular models](https://people.ucsc.edu/~warner/buffer.html)