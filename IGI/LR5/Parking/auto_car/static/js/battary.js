navigator.getBattery().then((battery) => {

  function updateAllBatteryInfo() {
    updateChargeInfo();
    updateLevelInfo();
    updateChargingInfo();
    updateDischargingInfo();
  }
  updateAllBatteryInfo();

  battery.addEventListener("chargingchange", updateChargeInfo);
  battery.addEventListener("levelchange", updateLevelInfo);
  battery.addEventListener("chargingtimechange", updateChargingInfo);
  battery.addEventListener("dischargingtimechange", updateDischargingInfo);

  function updateChargeInfo() {
    document.getElementById("chargeInfo").textContent =
      "Charging: " + (battery.charging ? "Yes" : "no");
  }

  function updateLevelInfo() {
    document.getElementById("levelInfo").textContent =
      "Level: " + battery.level * 100 + "%";
  }

  function updateChargingInfo() {
    document.getElementById("chargingTimeInfo").textContent =
      "Until charged: " + battery.chargingTime + " s";
  }

  function updateDischargingInfo() {
    document.getElementById("dischargingTimeInfo").textContent =
      "Until discharged: " + battery.dischargingTime + " s";
  }

});