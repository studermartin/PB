# Change to PyBricks

| Current | PyBricks | Comments |
| ------- | -------- | -------- |
| await ausführen_wand_seitlich(-2) | wall.rightTo(-20) | Comments |
| await warte(100) | wait(100) | |
| await gyro_fahren(-20, 1050, 90) | drive.turn_to_and_drive(-90,-200) | Change distance from cm to mm ; angle * -1 |
| await fahre_sekunden(0.4, 500) | drive.straigt_ms(4,500) | Change distance from cm to mm |
| await drehe_auf(140, Drehrichtung.GEGENUHRZEIGERSINN, Raeder.LINKS) | drive.rotate_to_backward(-140) | angle * -1 |
