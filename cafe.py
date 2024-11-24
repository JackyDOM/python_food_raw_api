from flask import jsonify

cafe = [
  {
    'id': 1,
    'cafe_name': 'Brown Coffee and Bakery',
    'cafe_image': '',
    'cafe_detail': {
      'cafe_name': 'Brown Coffee and Bakery',
      'cafe_image': '',
      'description': 'Brown Coffee ជាហាងកាហ្វេក្នុងស្រុកដ៏ល្បីមួយរបស់ប្រទេសកម្ពុជា ផ្តល់ជូននូវការបញ្ចូលគ្នានៃការរចនាបែបទំនើប និងបរិយាកាសស្វាគមន៍។ វាជាកន្លែងពេញនិយមសម្រាប់ទាំងអ្នកស្រុក និងជនបរទេស។',
      'location': 'សាខាជាច្រើននៅភ្នំពេញ សៀមរាប និងទីក្រុងធំៗផ្សេងទៀត។',
      'famous_drink': 'Iced Khmer Coffee (strong and sweet) and signature lattes.',
      'notableFeature': 'គ្រាប់កាហ្វេលីងក្នុងស្រុក ធានាជូននូវភេសជ្ជៈស្រស់ និងគុណភាព។ ផ្នែកខាងក្នុងដ៏កក់ក្ដៅជាមួយនឹងធាតុផ្សំនៃការរចនាបែបខ្មែរសហសម័យ។ Wi-Fi ឥតគិតថ្លៃ ធ្វើឱ្យវាក្លាយជាកន្លែងដ៏ល្អសម្រាប់ការងារ ឬការសិក្សា។',
    }
  },
  {
    'id': 2,
    'cafe_name': 'The Glasshouse Deli. Patisserie',
    'cafe_image': '',
    'cafe_detail': {
      'cafe_name': '',
      'cafe_image': '',
      'description': 'មានទីតាំងនៅក្នុងសណ្ឋាគារ Raffles Hotel Le Royal ដ៏ប្រណិត The Glasshouse ត្រូវបានគេស្គាល់ថាសម្រាប់កាហ្វេលំដាប់ថ្នាក់ខ្ពស់ កុម្មង់នំ និងបង្អែមដ៏រីករាយ។',
      'location': 'ភ្នំពេញ ប្រទេសកម្ពុជា។',
      'famous_drink': 'Artisan hot chocolate and cappuccino.',
      'notableFeature': 'បរិយាកាសដ៏ប្រណិត និងប្រណិត ល្អឥតខ្ចោះសម្រាប់កិច្ចប្រជុំផ្លូវការ ឬឱកាសពិសេស។ ផ្តល់ជូននូវនំកុម្មង់នំ និងនំដែលបំផុសគំនិតដោយអឺរ៉ុបជាច្រើន។ ទិដ្ឋភាពសួនច្បារដ៏ស្រស់ស្អាតសម្រាប់ការសម្រាកកាហ្វេដ៏ស្ងប់ស្ងាត់។',
    }
  },
  {
    'id': 3,
    'cafe_name': 'Sisters Srey Café',
    'cafe_image': '',
    'cafe_detail': {
      'cafe_name': 'Sisters Srey Café',
      'cafe_image': '',
      'description': 'ហាងកាហ្វេដែលគិតគូរពីសង្គម ដែលគាំទ្រសហគមន៍មូលដ្ឋាន និងផ្តល់នូវបរិយាកាសសម្រាកកាយ។ វាពេញនិយមក្នុងចំណោមអ្នកធ្វើដំណើរ និងអ្នកស្រុកដូចគ្នា។',
      'location': 'សៀមរាប ជិតផ្សារចាស់។',
      'famous_drink': 'Iced Coconut Coffee and Mango Smoothies.',
      'notableFeature': 'ផ្តោតលើនិរន្តរភាព និងគាំទ្រយុវជនកម្ពុជា តាមរយៈកម្មវិធីអប់រំ។ បម្រើ​ជម្រើស​សរីរាង្គ​ដែល​មាន​សុខភាព​ល្អ រួម​ទាំង​ចាន​បន្លែ​និង​គ្មាន​ជាតិ​ gluten។ កន្លែងអង្គុយបែបបណ្ណាល័យដ៏កក់ក្ដៅដែលមានសៀវភៅ និងសិប្បកម្មសម្រាប់លក់។',
    }
  },
  {
    'id': 4,
    'cafe_name': 'Blue Pumpkin',
    'cafe_image': '',
    'cafe_detail': {
      'cafe_name': 'Blue Pumpkin',
      'cafe_image': '',
      'description': 'Blue Pumpkin គឺជាការលាយបញ្ចូលគ្នានៃហាងកាហ្វេ ហាងនំប៉័ង និងការ៉េម ដែលផ្តល់ជូននូវភេសជ្ជៈ អាហារ និងបង្អែមជាច្រើនប្រភេទនៅក្នុងបរិយាកាសបែបទំនើប និងសម្រាកកាយ។',
      'location': 'សាខានៅភ្នំពេញ សៀមរាប និងបាត់ដំបង។',
      'famous_drink': 'Freshly squeezed fruit juices and milkshakes.',
      'notableFeature': 'ល្បី​សម្រាប់​ការ៉េម​ផលិត​នៅ​ផ្ទះ​និង gelato ។ ផ្នែកខាងក្នុងពណ៌សតូចបំផុត ជាមួយនឹងភាពរំជើបរំជួល។ កន្លែងអង្គុយបែបបែប Lounge ល្អឥតខ្ចោះសម្រាប់អង្គុយលេងជាមួយមិត្តភក្តិ ឬក្រុមគ្រួសារ។',
    }
  },
  {
    'id': 5,
    'cafe_name': 'Factory Coffee',
    'cafe_image': '',
    'cafe_detail': {
      'cafe_name': 'Factory Coffee',
      'cafe_image': '',
      'description': 'ហាងកាហ្វេដ៏ប្រណិតមួយដែលមានទីតាំងនៅកន្លែងធ្វើការរួមគ្នា និងកន្លែងរៀបចំព្រឹត្តិការណ៍។ វាទាក់ទាញអ្នកជំនាញវ័យក្មេង និងអ្នកច្នៃប្រឌិតដែលកំពុងស្វែងរកកាហ្វេដ៏អស្ចារ្យ និងបរិយាកាសដែលបំផុសគំនិត។',
      'location': 'Phnom Penh, Factory Phnom Penh (a creative hub near the city center).',
      'famous_drink': 'Nitro Cold Brew and Vietnamese-style Egg Coffee.',
      'notableFeature': 'ផ្ទៃខាងក្នុងបែបឧស្សាហកម្ម ជាមួយនឹងរុក្ខជាតិបៃតង និងទីធ្លាធំទូលាយ។ រៀបចំការតាំងពិពណ៌សិល្បៈ សិក្ខាសាលា និងព្រឹត្តិការណ៍តន្ត្រីជាទៀងទាត់។ ផ្តល់សិទ្ធិចូលទៅកន្លែងធ្វើការរួមគ្នាសម្រាប់អ្នកឯករាជ្យ និងសហគ្រិន។',
    }
  }
  
]

def get_cafe():
  response = {
        "status": 200,
        "message": "Temple retrieved successfully",
        "data": cafe,
    }
  return jsonify(response)