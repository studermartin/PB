# Change to PyBricks

| | Lego | PyBricks | Comments |
| ------- | ------- | -------- | -------- |
| Wall | await ausführen_wand_seitlich(-2) | wall.rightTo(-20) |  |
|  | start_wand_seitlich(-0.3) | wall.rightTo(-3, wait=False) | Change distance from cm to mm ; dont't wait |
|  | await ausführen_wand_vertikal(0.5) | wall.upTo(5) | Change distance from cm to mm |
|  | start_wand_vertikal(6) | wall.upTo(60), wait=False) | Change distance from cm to mm |
| Wait | await warte(100) | wait(100) | |
| Drive | await gyro_fahren(-20, 1050, 90) | drive.drive_to(-90,-200) | Change distance from cm to mm ; angle * -1 |
|  | await fahre_sekunden(0.4, 500) | drive.straigt_ms(4,500) | Change distance from cm to mm |
| Turn | await drehe_auf(140, Drehrichtung.GEGENUHRZEIGERSINN, Raeder.LINKS) | drive.rotate_to_backward(-140) | angle * -1 |
