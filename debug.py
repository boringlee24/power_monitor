from carbontracker.tracker import CarbonTracker, CarbonTrackerManual
import time
info={}
tracker = CarbonTrackerManual(epochs=1, monitor_epochs=1, update_interval=0.1,
    components='all', epochs_before_pred=1, verbose=0)
tracker.tracker.pue_manual=1
tracker.intensity_updater.ci_manual = 100
time.sleep(5) # give it some cushion to initialize measurement
for i in (range(20)):
    tracker.epoch_start()
    print(f"Prompt {i}")
    time.sleep(0.5)    
    energy, co2, duration = tracker.epoch_end('')
    info[i] = {
        "Energy": energy,
        "CO2": co2,
        "Duration": duration,
    }
print(info)





