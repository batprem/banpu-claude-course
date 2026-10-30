# UC3 · รวมข้อมูล ESG จากหลาย Site (ESG Data Consolidation)
> ข้อมูลสมมติเพื่อการอบรมเท่านั้น (synthetic) ไม่ใช่ข้อมูลจริงของบ้านปู · ทำสำเนาก่อนให้ Claude แก้ (copy-before-write)

**เจ้าของโจทย์ (สมมติ):** ทีม ESG รวบรวมข้อมูลพลังงาน น้ำ และการปล่อยก๊าซจาก 4 Site ทุกปี แต่ละ Site ส่งไฟล์คนละรูปแบบ คนละหน่วย คนละความถี่

| Canvas | ตั้งต้น (ทีมปรับได้) |
|---|---|
| Data | `site_A_energy_water_2568.xlsx` (kWh, ลิตร) · `site_C_esg_2568.csv` (MWh, ตัน) · `site_F_solar_2568.xlsx` (รายไตรมาส) · `site_G_utilities_2568.csv` (MMBtu) · `emission_factors_SYNTHETIC.csv` · `esg_targets_2568.csv` |
| Connector | วันจริง: SharePoint folder ที่แต่ละ Site อัปโหลด · วันนี้: โฟลเดอร์ใน Cowork |
| Output | ตารางรวมหน่วยเดียวกัน + tCO2e (ค่าสมมติ) เทียบเป้า + Dashboard Artifact 1 หน้า (M4) |
| Trade-off | ค่า emission factor ในไฟล์เป็น**ค่าสมมติ** ห้ามใช้ทางการ · ข้อมูลหาย/ประมาณ ต้องระบุในรายงาน ไม่ให้ AI เติมเอง |

**เกณฑ์เสร็จ:** ตารางแปลงหน่วยแสดงสูตร · ระบุครบ 3 ข้อสังเกต (Site G ขาด ต.ค. · Site F รายไตรมาส · Site A ก.ค. มิเตอร์เสีย) · ทุกตัวเลขรวมตรวจย้อนได้
**ต่อยอด:** Workshop B ของ M2 (Excel กระจัดกระจาย) · Dashboard refresh (M6)
**Prompt เริ่มต้น:** `M7-P06`
