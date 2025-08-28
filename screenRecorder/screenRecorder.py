import mss
import numpy as np
import cv2
import time
import os 

def screen_recorder(duration=10, output_path="video.mp4", fps=20.0):

    if output_path is None:
        output_dir = os.path.expanduser("~/AutoBongPy/video")
        os.makedirs(output_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(output_dir, f"capture_{timestamp}.mp4")

    with mss.mss() as sct:
        monitor = sct.monitors[1]  # écran principal
        screen_width = monitor['width']
        screen_height = monitor['height']

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        output = cv2.VideoWriter(output_path, fourcc, fps, (screen_width, screen_height))

        end_time = time.time() + duration

        print(f"Enregistrement de l'écran pendant {duration} secondes...")
        print(f"Fichier sauvegardé dans : {output_path}")

        try:
            while time.time() < end_time:
                img = sct.grab(monitor)
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR) 

                output.write(frame)

                if cv2.waitKey(1) == ord('q'):
                    print("Arrêt anticipé.")
                    break

        finally:
            output.release()
            cv2.destroyAllWindows()
            print("Enregistrement terminé.")
