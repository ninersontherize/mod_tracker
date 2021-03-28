from app import app

#TO-DO add fixtures to isolate this test from changing db
def test_mods():
  tester = app.test_client()
  response = tester.get("/mods", content_type="html/text")

  assert response.status_code == 200
  assert response.data == b"""{
  "mods": [
    {
      "installed": false, 
      "link": "https://www.systemmotorsports.com/collections/fk8-civic-type-r-wheel-fitment-2017/products/rays-volk-te37-saga-18x9-5-33-5x120-face-4-concave-2017-civic-type-r-fk8-fitment", 
      "part_name": "Volk Racing TE37 18-inch", 
      "price": "$3,473.20", 
      "purchased": false, 
      "section": "wheels"
    }, 
    {
      "installed": false, 
      "link": "https://www.tirerack.com/tires/tires.jsp?tireMake=Michelin&tireModel=Pilot+Sport+Cup+2", 
      "part_name": "Michelin ", 
      "price": "$1569.12", 
      "purchased": false, 
      "section": "tires"
    }, 
    {
      "installed": false, 
      "link": "https://www.tirerack.com/tires/tires.jsp?tireMake=Pirelli&tireModel=P+Zero+Trofeo+R&partnum=44YR8P0TRXL&vehicleSearch=true&fromCompare1=yes&autoMake=Honda&autoYear=2021&autoModel=Civic%20Type%20R&autoModClar=", 
      "part_name": "Pirelli P Zero Trofeo R", 
      "price": "$1208.80", 
      "purchased": false, 
      "section": "tires"
    }, 
    {
      "installed": false, 
      "link": "https://www.systemmotorsports.com/collections/fk8-civic-type-r-wheel-fitment-2017/products/rays-volk-racing-ze40-rw-limited-18x10-36-5x120-4-wheels", 
      "part_name": "Volk Racing ZE40 RW LIMITED 18X10", 
      "price": "$3,350.00", 
      "purchased": false, 
      "section": "wheels"
    }
  ], 
  "status": "success"
}
"""