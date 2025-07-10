# IX-ZeroCell – Regulated Output Stage

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Boost supercapacitor voltage to regulated output (3.3V or 5V) for powering external devices

---

## 🔋 Input Source

| Input          | Spec                      |
|----------------|---------------------------|
| Source Voltage | 0.6V – 5.4V (supercap)  
| Input Cap      | 100µF + 10nF (parallel)  
| ESR Target     | < 50mΩ  

---

## ⚙️ Output Targets

| Rail         | Target Voltage | Max Current | Use Case                      |
|--------------|----------------|-------------|-------------------------------|
| Primary Rail | 3.3V           | 200–500mA   | Logic, sensors, low-power SoC  
| Optional USB | 5.0V           | 100–300mA   | Trickle USB, BLE TX burst  

---

## ⚡ Boost Converter IC (Example)

| IC Name       | Value              |
|---------------|--------------------|
| Recommended   | TPS61200 (TI)  
| Alt. Choice   | MT3608 (Cheap)  
| Startup Vmin  | 0.3–0.8V  
| Switch Freq.  | 500kHz–1.2MHz  
| Efficiency    | 75–90%  

---

## 🛠️ Boost Stage Components

| Component        | Value / Notes                |
|------------------|------------------------------|
| L1 (Inductor)     | 4.7µH – 10µH, low DCR  
| Cin (Input Cap)   | 100µF low ESR + 10nF  
| Cout (Output Cap) | 22µF ceramic ×2  
| D1 (Schottky)     | SS14 or MBRS340  
| Feedback R1/R2    | Set based on desired Vout  
| EN Pin Pullup     | 100kΩ to Vin or Vout  
| Soft-start Cap    | 100nF (if supported by IC)  

---

## 🔌 Output Protection / Extras

| Feature            | Component         | Notes                          |
|--------------------|------------------|--------------------------------|
| USB Port Option     | Female USB-A     | Powered by 5V output  
| ESD TVS Diode       | PESD3V3L1BA or similar | Protects against surge  
| Output LED          | Red w/ 1kΩ       | Status indicator  
| Switch (optional)   | SPDT toggle      | Cuts Vin to Boost when off  

---

## 📈 Output Performance

| Cap Charge (%) | Vcap     | Boost Output | Notes                          |
|----------------|----------|--------------|--------------------------------|
| ~15%           | ~0.9V    | ~2.8V        | May fail to reach regulation  
| ~40%           | ~2.2V    | 3.3V stable  | Regulated 3.3V begins  
| ~60%+          | ~3.5V+   | 5.0V (USB)   | USB-level voltage enabled  

---

## 🔋 USB Output Considerations

- Output current is **limited by cap bank + boost IC rating**  
- Can charge low-draw items: BLE devices, earbuds, trickle-charging phones  
- Should not exceed ~300mA  
- Add inline polyfuse (500mA PTC) for protection

---

## 🔧 PCB Guidelines

- Keep feedback lines short  
- Shield sensitive analog traces from inductor EMI  
- Separate high-current input/output planes  
- Use copper pour for ground under boost IC  
- Ensure thermal relief if using high-draw mode (>200mA)

---

## 🔄 Real-World Use Examples

| Scenario                    | Device Powered       | Duration     |
|-----------------------------|----------------------|--------------|
| BLE Temp Sensor             | 3.3V @ 50mA avg      | 3–6 hrs  
| Arduino Nano (low power)    | 3.3V @ 70mA          | 1–2 hrs  
| ESP32 deep sleep cycles     | 3.3V burst @ 150mA   | 50–120 wake cycles  
| USB fan / LED               | 5V @ 150mA           | 1–3 minutes  
| Mobile phone (USB trickle)  | 5V @ 250mA           | 2–5% boost  

---

## ✅ Summary

- Boosts ambient-harvested supercap energy to 3.3V or 5V  
- Uses proven boost converter ICs (TPS61200, MT3608)  
- Passive startup from as low as 0.3V  
- Ideal for IoT, sensors, USB power, small MCUs  
- Fully protected, fully modular

