# Change to PyBricks

| | Lego | PyBricks | Comments |
| ------- | ------- | -------- | -------- |
| Wall | await ausführen_wand_seitlich(-2) | wall.rightTo(-20) |  |
|  | start_wand_seitlich(-0.3) | wall.rightTo(-3, wait=False) | Change distance from cm to mm ; dont't wait |
|  | await ausführen_wand_vertikal(0.5) | wall.upTo(5) | Change distance from cm to mm |
|  | start_wand_vertikal(6) | wall.upTo(60, wait=False) | Change distance from cm to mm |
| Wait | await warte(100) | wait(100) | |
| Drive | await gyro_fahren(-20, 1050, 90) | drive.drive_to(-90,-200) | Exchange parameter 1 and 3; change distance from cm to mm ; angle * -1 |
|  | await fahre_sekunden(0.4, 500) | drive.straigt_ms(4,500) | Change distance from cm to mm |
| Turn | await drehe_auf(140, Drehrichtung.GEGENUHRZEIGERSINN, Raeder.LINKS) | drive.rotate_to_backward(-140) | angle * -1 |
|  | await drehe_auf(14, Drehrichtung.GEGENUHRZEIGERSINN, Raeder.RECHTS) | drive.rotate_to_forward(-14) | angle * -1 |
|  | await drehe_auf(-15, Drehrichtung.UHRZEIGERSINN, Raeder.LINKS) | drive.rotate_to_backward(15) | angle * -1 |

# Default Translating of Driving Speeds
| Lego | PyBricks | Comments |
| ------- | ------- | -------- |
| 1050 | 400 | Max. speed |
| 1000 | 380 |  |
| 900 | 350 | |
| 800 | 300 |  |
| 700 | 260 |  |
| 600 | 230 |  |
| 500 | 190 |  |
| 400 | 160 |  |
| 300 | 110 |  |
| 200 | 75 |  |
| 100 | 40 |  |

# Default Translating of Wall Speeds
| Lego | PyBricks | Comments |
| ------- | ------- | -------- |
| 1000 | 50 | Default speed |
| 500 | 25 | Default speed |
| 200 | 10 | Default speed |
