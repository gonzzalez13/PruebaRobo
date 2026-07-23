from robobopy.Robobo import Robobo
from robobopy.utils.BlobColor import BlobColor

from behaviour_mod.buscar_color import BuscarColor
from behaviour_mod.moverse_color import MoverseColor
import time


def main():
    rob = Robobo("Localhost")
    rob.connect()
    rob.resetColorBlobs()

    rob.setActiveBlobs(True,False,False,False)

    params = {"stop": False}

    #Crar los comportamientos
    BuscarColor_behaviour = BuscarColor(rob,[],params,BlobColor.RED)
    MoverseColor_behaviour = MoverseColor(rob,[BuscarColor_behaviour],params)


    threads = [BuscarColor_behaviour,MoverseColor_behaviour]

    BuscarColor_behaviour.start()
    MoverseColor_behaviour.start()

    while not params["stop"]:
        time.sleep(0.1)


    for thread in threads:
        thread.join()




if __name__ == "__main__":
    main()
