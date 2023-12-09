# Snake-DeepQ-Learning

## Reference to [chuyangliu/snake](https://github.com/chuyangliu/snake)
In this project, we develop additional wall modes to evaluate the effectiveness of each snake's walking strategy (greedy, hamilton, deep Q-network).
## Overview
### Define wall modes (map size 8x8)
| Wall mode | Description                        |
| :-------: | ---------------------------------- |
|     0     | no walls                           |
|     1     | 4 walls are located near 4 corners |
|     2     | 8 walls form 2 parallel lines      |
|     3     | 8 random walls                     |

### Results (map size 8x8)
| Wall mode |                Visualization                 |                                Hamilton                                |                      Greedy<br/>(Step limit: 2.000)                      |             Deep Q-network<br/>(Training step: 3.000.000)              |
| :-------: | :------------------------------------------: | :--------------------------------------------------------------------: | :----------------------------------------------------------------------: | :--------------------------------------------------------------------: |
|     0     | <img src="./docs/wall mode 0.gif" width=200> | Average Length: 64.00<br/>Average Steps: 718.33<br/>Steps/length: 11.2 |  Average Length: 59.72<br/>Average Steps: 719.48<br/>Steps/length: 12.0  | Average Length: 24.44<br/>Average Steps: 131.69<br/>Steps/length: 5.39 |
|     1     | <img src="./docs/wall mode 1.gif" width=200> |                              Unavailable                               | Average Length: 46.04<br/>Average Steps: 1754.70<br/>Steps/length: 38.11 |                              Unavailable                               |
|     2     | <img src="./docs/wall mode 2.gif" width=200> |                              Unavailable                               |  Average Length: 51.11<br/>Average Steps: 681.03<br/>Steps/length: 13.3  | Average Length: 23.21<br/>Average Steps: 165.12<br/>Steps/length: 7.11 |
|     3     | <img src="./docs/wall mode 3.gif" width=200> |                              Unavailable                               | Average Length: 37.27<br/>Average Steps: 1692.71<br/>Steps/length: 45.4  | Average Length: 21.62<br/>Average Steps: 158.40<br/>Steps/length: 7.33 |

## How to run
```
python run.py
```

Table of arguments:
| Argument |  Meaning  |                Options                 | Default  |
| :------: | :-------: | :------------------------------------: | :------: |
|    -s    |  solver   |        [greedy, hamilton, dqn]         | hamilton |
|    -m    |   mode    | [play, bcmk, train_dqn, train_dqn_gui] |   play   |
|    -w    | wall mode |              [0, 1, 2, 3]              |    0     |
|    -p    | map size  |              [8, 12, 24]               |    8     |

For example, if you want to run the DeepQ solver on wall mode 2 and map size 8x8. Then
```
python run.py -s dqn -w 2
```

## How to train
Training deep Q-network without GUI
```
python run.py -s train_dqn
```
or training deep Q-network with GUI
```
python run.py -s train_dqn_gui
```

## Contact
If you have any question, please email ngoduythinh250601@gmail.com or email pna2791@gmail.com.