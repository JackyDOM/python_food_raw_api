from flask import jsonify, Response
import json


foods = [
  {
    'id': 1,
    'food_name': 'អាម៉ុកត្រី',
    'food_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTI03eoZIeL23drbKYpir9l6cNygyjufDXtI7fhTF19-osQ1xIJ0eh5a3r4jr8CB0kEo6s&usqp=CAU',
    'category': {
      'category_name': 'Dish'
    },
    'detail': {
      'food_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTI03eoZIeL23drbKYpir9l6cNygyjufDXtI7fhTF19-osQ1xIJ0eh5a3r4jr8CB0kEo6s&usqp=CAU',
      'food_name': 'អាម៉ុកត្រី',
      'ingredient': 'សាច់ត្រីស្រស់ (ឧ. ត្រីខ ឬត្រីស), ទឹកដោះគោដូង, ស្លឹកគ្រៃ, ស្លឹក Kaffir lime, Galangal,រមៀត,ខ្ទឹម,សាឡុត,ម្ទេសក្រហម,ទឹកត្រី,ស្លឹកចេក (សម្រាប់រុំ)',
      'description': '''ត្រីអាម៉ុក គឺជាមុខម្ហូបដ៏ល្បីបំផុតមួយរបស់ប្រទេសកម្ពុជា គឺការីត្រីក្រអូបចំហុយស្លឹកចេក។ ម្ហូបនេះមានសាច់ក្រែម និងសម្បូរដោយទឹកដោះគោដូង ហើយត្រូវបានបញ្ចូលទៅដោយក្លិនក្រអូបនៃឱសថស្រស់ៗ និងគ្រឿងទេសដូចជាស្លឹកគ្រៃ និងក្រូចឆ្មា។ បម្រើតាមបែបប្រពៃណីជាមួយបាយ វាគឺជាការលាយបញ្ចូលគ្នានៃរសជាតិផ្អែម រសជាតិ និងហឹរបន្តិច។''',
      'receipe': 'ដើម្បីធ្វើអាម៉ុកត្រយ (ត្រីអាម៉ុក) លាយស្លឹកគ្រៃ ស្លឹកក្រូចសើច ស្លឹកខ្ទឹម រមៀត ខ្ទឹមស ខ្ទឹមក្រហម និងម្ទេសក្រហម បុកចូលទឹកខ្ទិះដូង ទឹកត្រី និងត្រីស្រស់ហាន់ជាចំនិត។ 15នាទី ចាក់ល្បាយចូលក្នុងចានស្លឹកចេក ឬខ្ចប់ ចំហុយ 20-25នាទី រហូតទាល់តែរឹងមាំ សឹមទទួលទានជាមួយក្រូចឆ្មារ ស្លឹកខ្ទឹម និងអង្ករ។',
    }
  },
  {
    'id': 2,
    'food_name': 'បាយសាច់ជ្រូក',
    'food_image': 'https://images.deliveryhero.io/image/fd-kh/Products/1008386.jpg?width=%s',
    'category': {
      'category_name': 'Dish'
    },
    'detail': {
      'food_image': 'https://images.deliveryhero.io/image/fd-kh/Products/1008386.jpg?width=%s',
      'food_name': 'បាយសាច់ជ្រូក',
      'ingredient': 'ខ្ទឹម, ទឹកដោះគោដូង, ទឹកត្រី, ស្ករត្នោត, ទឹកស៊ីអ៊ីវ, អង្ករសចំហុយ, បន្លែជ្រក់ (ឧ. ត្រសក់ ការ៉ុត), ទំពាំងបាយជូរឬស៊ុប (បម្រើនៅចំហៀង)',
      'description': 'បាយសឈូក គឺជាមុខម្ហូបអាហារពេលព្រឹកដ៏ពេញនិយមមួយនៅក្នុងប្រទេសកម្ពុជា ដែលមានសាច់ជ្រូកអាំងដុតឱ្យល្អឥតខ្ចោះ និងបម្រើលើបាយចំហុយ។ សាច់​ជ្រូក​មាន​រសជាតិ​ឈ្ងុយ ផ្អែម​បន្តិច និង​មាន​ក្លិន​ឈ្ងុយ ដែល​ធ្វើ​ឱ្យ​វា​ជា​អាហារ​ដែល​ផ្តល់​ផាសុកភាព និង​ពេញចិត្ត។ ម្ហូបនេះត្រូវបានអមដោយបន្លែជ្រក់ និងទំពាំងបាយជូរស្រាលៗ ដើម្បីរក្សាតុល្យភាពរសជាតិ។ វាសាមញ្ញ តែសំបូរទៅដោយរសជាតិប្រពៃណីខ្មែរ។',
      'receipe': 'ដើម្បីធ្វើបាយសឈូក (សាច់ជ្រូក និងបាយ) ដាក់សាច់ជ្រូកហាន់ជាបន្ទះស្តើងៗ ខ្ទឹមក្រហម ទឹកដោះគោ ទឹកត្រី ស្ករត្នោត និងទឹកស៊ីអ៊ីវ ដុតឲ្យម៉ដ្ឋ រួចដាក់អង្ករសចំហុយជាមួយបន្លែជ្រក់ និងទឹកស៊ុបមួយចំហៀង',
    }
  },
  {
    'id': 3,
    'food_name': 'នំអន្សមចេក',
    'food_image': 'https://huunghivietnamcampuchia.thoidai.com.vn/stores/news_dataimages/huunghivietnamcampuchia-thoidai-com-vn/092020/17/15/fn-2020-09-17-12-00-46-020210111140811.9412520.jpg',
    'category': {
      'category_name': 'Dessert'
    },
    'detail': {
      'food_image': 'https://huunghivietnamcampuchia.thoidai.com.vn/stores/news_dataimages/huunghivietnamcampuchia-thoidai-com-vn/092020/17/15/fn-2020-09-17-12-00-46-020210111140811.9412520.jpg',
      'food_name': 'នំអន្សមចេក',
      'ingredient': 'អង្ករដំណើប, ចេកទុំ (ជាធម្មតាផ្អែមដូចជាប្រភេទ "Cavendish"), ខ្ទិះដូង (សម្រាប់បំពេញ), ស្ករត្នោត ឬស្ករធម្មតា (សម្រាប់ផ្អែម), ស្លឹកចេក (សម្រាប់រុំ)',
      'description': 'នំអន្សមចេក ជា​បង្អែម​ប្រពៃណី​ខ្មែរ​ដែល​ធ្វើ​ពី​អង្ករ​ដំណើប ចេក និង​ដូង។ វាជាអាហារដ៏ពេញនិយម ជាពិសេសក្នុងឱកាសចូលឆ្នាំខ្មែរ និងឱកាសពិសេសផ្សេងៗ។ បង្អែម​ត្រូវ​បាន​រុំ​ដោយ​ស្លឹក​ចេក រួច​ចំហុយ​ឲ្យ​បាន​គ្រប់​លក្ខណៈ។ ការរួមផ្សំនៃចេកផ្អែមជាមួយនឹងអង្ករដំណើប និងដូងសម្បូរបែប ធ្វើឱ្យវាក្លាយជាបង្អែមដែលមានរសជាតិ និងពេញចិត្ត។',
      'receipe': 'ដើម្បីធ្វើនំអន្សមចេក លាយអង្ករដំណើបជាមួយខ្ទិះដូង និងស្ករស រុំចេកទុំក្នុងល្បាយដោយប្រើស្លឹកចេក បិទឱ្យជិត ចំហុយរហូតទាល់តែឆ្អិន រួចទទួលទានអាហារខ្មែរដ៏ផ្អែមនេះ។',
    }
  },
  {
    'id': 4,
    'food_name': 'ចេកខ្វិះ',
    'food_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBftPEdIqANix2WyctJx-raBLNWLQXztS2hw&s',
    'category': {
      'category_name': 'Dessert'
    },
    'detail': {
      'food_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBftPEdIqANix2WyctJx-raBLNWLQXztS2hw&s',
      'food_name': 'ចេកខ្វិះ',
      'ingredient': 'ចេកទុំ, ទឹកដោះគោដូង, ស្ករត្នោត (ឬស្ករធម្មតា), អំបិលមួយក្តាប់ (ដើម្បីបង្កើនរសជាតិ)',
      'description': 'ចេកខ្វិះ ជា​បង្អែម​ខ្មែរ​ពិសេស​មួយ​ដែល​មាន​ផ្លែ​ចេក​ក្នុង​ទឹក​ខ្ទិះដូង។ ចេក​ត្រូវ​បាន​ស្ងោរ​ក្នុង​ល្បាយ​ទឹកដោះគោ​ដូង​ដែល​មាន​រសជាតិ​ផ្អែម​ឆ្ងាញ់ ដែល​មនុស្ស​ជា​ច្រើន​ចូលចិត្ត ជាពិសេស​នៅ​តាម​ជនបទ។ វា​ជា​បង្អែម​ដ៏​សាមញ្ញ ប៉ុន្តែ​មាន​រសជាតិ​ឆ្ងាញ់ ដែល​ផ្តល់​នូវ​តុល្យភាព​ដ៏​ល្អឥតខ្ចោះ​នៃ​ភាពផ្អែម និង​ភាពសម្បូរបែប។',
      'receipe': 'ដើម្បី​ធ្វើ​ចេកខ្វិះ ត្រូវ​យក​ចេក​ទុំ​ដាក់​ក្នុង​ទឹកដោះគោ​ដូង​ផ្អែម​ជាមួយ​ស្ករត្នោត និង​អំបិល​បន្តិច​រហូត​ដល់​ចេក​ទន់​ហើយ​ទឹកជ្រលក់​ឡើង​ក្រាស់ រួច​យក​ទៅ​ធ្វើ​ជា​បង្អែម​ខ្មែរ​បែប​ក្តៅ​ៗ ។'
    }
  },
  {
    'id': 5,
    'food_name': 'គុយទាវ',
    'food_image': 'https://images.deliveryhero.io/image/fd-kh/LH/xg31-hero.jpg?width=512&height=384&quality=45',
    'category': {
      'category_name': 'Soup'
    },
    'detail': {
      'food_image': 'https://images.deliveryhero.io/image/fd-kh/LH/xg31-hero.jpg?width=512&height=384&quality=45',
      'food_name': 'គុយទាវ',
      'ingredient': 'គុយទាវ, សាច់មាន់ សាច់ជ្រូក ឬសាច់គោ (ឬសាច់ចម្រុះ), ខ្ទឹម, ខ្ទឹមបារាំង, ស្លឹកគ្រៃ, ទឹកត្រី, អំបិលនិងស្ករ, ឱសថស្រស់ៗ (ជីវ៉ាន់ស៊ុយថៃ ជីអង្កាម), ក្រូចឆ្មារ, ម្ទេស (ជាជម្រើសសម្រាប់កំដៅ), ខ្ទឹម​ស ឬ​ខ្ទឹម​ស (សម្រាប់​គ្រឿង​លម្អ)',
      'description': 'គុយទាវ គឺជាគុយទាវដ៏ពេញនិយមរបស់ខ្មែរ ដែលតែងតែបម្រើជាអាហារពេលព្រឹក ប៉ុន្តែអាចទទួលទានបានគ្រប់ពេលនៃថ្ងៃ។ ស៊ុប​នេះ​ត្រូវ​បាន​ផលិត​ឡើង​ដោយ​ទឹក​ទំពាំងបាយជូរ​ស្រាល និង​មាន​ក្លិន​ឈ្ងុយ ដែល​ជា​ធម្មតា​មាន​រសជាតិ​ជាមួយ​នឹង​សាច់មាន់ សាច់ជ្រូក ឬ​សាច់គោ ហើយ​តុបតែង​ដោយ​ឱសថ​ស្រស់ កំបោរ និង​ម្ទេស។ វា​ជា​ម្ហូប​ដែល​មាន​ផាសុកភាព និង​មាន​ច្រើន​មុខ​ដែល​ប្រជាជន​កម្ពុជា​ជាច្រើន​ចូលចិត្ត។',
      'receipe': 'ដើម្បី​ធ្វើ​គុយទាវ ត្រូវ​រៀបចំ​ទំពាំងបាយជូរ​រសជាតិ​ដោយ​ដាក់​សាច់មាន់ សាច់ជ្រូក ឬ​សាច់គោ​ជាមួយ​ខ្ទឹមស ខ្ទឹមបារាំង ស្លឹកគ្រៃ ទឹកត្រី អំបិល និង​ស្ករ​។ ចម្អិនគុយទាវដោយឡែកពីគ្នា បន្ទាប់មកដាក់គុយទាវចូលចានមួយ ចាក់ទឹកស៊ុបក្តៅៗពីលើ ហើយដាក់គ្រឿងក្រអូបស្រស់ ក្រូចឆ្មារ ខ្ទឹមក្រហម និងម្ទេសតាមការចង់បាន។',
    }
  },
  {
    'id': 6,
    'food_name': 'សម្លកកូ',
    'food_image': 'https://thukphadanet.wordpress.com/wp-content/uploads/2015/01/16-08-2014.jpg',
    'category': {
      'category_name': 'Soup'
    },
    'detail': {
      'food_image': 'https://thukphadanet.wordpress.com/wp-content/uploads/2015/01/16-08-2014.jpg',
      'food_name': 'សម្លកកូ',
      'ingredient': 'ម្សៅគ្រើម (ស្លឹកគ្រៃ ស្លឹកគ្រៃ រមៀត), សាច់ជ្រូក ឬត្រី (ជាជម្រើស), ម្សៅអង្ករលីង (សម្រាប់ក្រាស់), ពងទា, ផ្លែល្ហុងបៃតង, សណ្តែកវែង, ល្ពៅឬមឹក, ទឹកត្រី, អំបិលនិងស្ករ, ឱសថស្រស់ៗ (ស្លឹកខ្ទឹម)',
      'receipe': 'ដើម្បី​ធ្វើ​សម្លកកូ ត្រូវ​ប្រឡាក់​គ្រឿង​ក្រៀម​ក្នុង​ឆ្នាំង​រហូត​មាន​ក្លិន​ឈ្ងុយ រួច​ដាក់​សាច់ជ្រូក ឬ​ត្រី (បើ​ប្រើ) ហើយ​ចម្អិន​រហូត​ដល់​មាន​ពណ៌​ត្នោត​ស្រាល។ បន្ថែមទឹក ម្សៅអង្ករលីងអោយក្រាស់ រួចច្របល់ជាមួយទឹកត្រី អំបិល និងស្ករ។ បន្ថែមបន្លែ - ពងមាន់ ល្ហុងបៃតង សណ្តែកវែង និងល្ពៅ - ហើយដាំឱ្យពុះរហូតដល់ទន់។ បញ្ចប់ជាមួយនឹងឱសថស្រស់ៗដូចជា ស្លឹកខ្ទឹម និង basil ថៃមុនពេលបម្រើ។'
    }
  }
]

def get_food():
  response = {
        "status": 200,
        "message": "foods retrieved successfully",
        "data": foods,
    }
   # Pretty print the JSON response
  pretty_json = json.dumps(response, indent=4, ensure_ascii=False)
  return Response(pretty_json, content_type='application/json')