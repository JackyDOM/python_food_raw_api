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
      'food_image_detail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTI03eoZIeL23drbKYpir9l6cNygyjufDXtI7fhTF19-osQ1xIJ0eh5a3r4jr8CB0kEo6s&usqp=CAU',
      'food_image_detail': 'https://archphkai.wordpress.com/wp-content/uploads/2011/05/amok-thai.jpg',
      'food_image_detail': 'https://vareone.wordpress.com/wp-content/uploads/2015/08/1379560_710488079063359_5357890317022268593_n.jpg',
      'food_name': 'អាម៉ុកត្រី',
      'food_name_english': 'Amok Fish',
      'description': '''ត្រីអាម៉ុក គឺជាមុខម្ហូបដ៏ល្បីបំផុតមួយរបស់ប្រទេសកម្ពុជា គឺការីត្រីក្រអូបចំហុយស្លឹកចេក។ ម្ហូបនេះមានសាច់ក្រែម និងសម្បូរដោយទឹកដោះគោដូង ហើយត្រូវបានបញ្ចូលទៅដោយក្លិនក្រអូបនៃឱសថស្រស់ៗ និងគ្រឿងទេសដូចជាស្លឹកគ្រៃ និងក្រូចឆ្មា។ បម្រើតាមបែបប្រពៃណីជាមួយបាយ វាគឺជាការលាយបញ្ចូលគ្នានៃរសជាតិផ្អែម រសជាតិ និងហឹរបន្តិច។''',
      'ingredient': [
        {
          'id': 100,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_HYm-lS8ZIU2ISa5pj59TuryF74T0YMCTqw&s',
          'ingredient_name': 'សាច់ត្រីស្រស់'
        },
        {
          'id': 101,
          'ingredient_image': 'https://cdn.sabay.com/cdn/media.sabay.com/media/TECH-KK/SOVATH/Sep-2020-07/5f97de48d359a_1603788360_medium.jpg',
          'ingredient_name': 'ទឹកដោះគោ'
        },
        {
          'id': 102,
          'ingredient_image': 'https://sokhakrom.com/prms/uploads/plants/Capturekkl.PNG',
          'ingredient_name': 'ដូង'
        },
        {
          'id': 103,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyvK5WPC1N9HuVlsHKxkGRMiGubGG_IxupwA&s',
          'ingredient_name': 'ស្លឹកគ្រៃ'
        },
        {
          'id': 104,
          'ingredient_image': 'https://tokke.kesspay.io/storage/product/57448/2cdfe345e60eb3fcde505f4c9626ecc6a26c08f1.jpg',
          'ingredient_name': 'ស្លឹក Kaffir lime'
        },
        {
          'id': 105,
          'ingredient_image': 'https://www.thespruceeats.com/thmb/VxSEs6tcxGXbwjl8SgTvPOXmBew=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/what-is-galangal-5186943_Hero_01-9decd6d115ce495ab7d04464269ff5ef.jpg',
          'ingredient_name': 'Galangal'
        },
        {
          'id': 106,
          'ingredient_image': 'https://lh4.googleusercontent.com/proxy/F18mYKxvOO5YMV53p16rbLr55vKbKDsz_jOQkzCL1NgTmdtfHma3Cn0Tu7dGmDpVgbM9yX4Fy_wPt6RELugXLCbNzbTxxb8oGfCppYp2H03Sh_QpYe2QtElr5x8RPQq_PXJMFfvs_fpzJHO6STqbpogmnBrU3sfy2A',
          'ingredient_name': 'រមៀត'
        },
        {
          'id': 107,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZR6XmYagigMKMTt1yIm8JNoaGv0w36RI6rQ&s',
          'ingredient_name': 'ខ្ទឹម'
        },
        {
          'id': 108,
          'ingredient_image': 'https://domnor.com/admin/images/product/2022-09-08-00-49-55_1.jpg?v=1',
          'ingredient_name': 'សាឡាត'
        },
        {
          'id': 109,
          'ingredient_image': 'https://kohsantepheapdaily.com.kh/wp-content/images/2020/02/c9f0f895fb98ab9159f51fd0297e236d-9.jpg',
          'ingredient_name': 'ម្ទេសក្រហម'
        },
        {
          'id': 110,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzKl35ryMt7obQ5kQ5Nn0zl_ArOSQhHVXXrQ&s',
          'ingredient_name': 'ទឹកត្រី'
        },
        {
          'id': 111,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrSORHZQ8lNx4Q1UyvUH8xvwM7Mb-K0WzMYA&s',
          'ingredient_name': 'ស្លឹកចេក'
        }
      ],
      'video': {
        'video_cooking': 'https://youtu.be/mlngdPqXi10?si=QGfswMN52O9j89_S',
        'receipe': 'ដើម្បីធ្វើអាម៉ុកត្រយ (ត្រីអាម៉ុក) លាយស្លឹកគ្រៃ ស្លឹកក្រូចសើច ស្លឹកខ្ទឹម រមៀត ខ្ទឹមស ខ្ទឹមក្រហម និងម្ទេសក្រហម បុកចូលទឹកខ្ទិះដូង ទឹកត្រី និងត្រីស្រស់ហាន់ជាចំនិត។ 15នាទី ចាក់ល្បាយចូលក្នុងចានស្លឹកចេក ឬខ្ចប់ ចំហុយ 20-25នាទី រហូតទាល់តែរឹងមាំ សឹមទទួលទានជាមួយក្រូចឆ្មារ ស្លឹកខ្ទឹម និងអង្ករ។',
      }
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
      'food_image_detail': 'https://images.deliveryhero.io/image/fd-kh/Products/1008386.jpg?width=%s',
      'food_image_detail': 'https://images.deliveryhero.io/image/fd-kh/Products/1008386.jpg?width=%s',
      'food_image_detail': 'https://images.deliveryhero.io/image/fd-kh/Products/1008386.jpg?width=%s',
      'food_name': 'បាយសាច់ជ្រូក',
      'food_name_english': 'Pork rice',
      'description': 'បាយសឈូក គឺជាមុខម្ហូបអាហារពេលព្រឹកដ៏ពេញនិយមមួយនៅក្នុងប្រទេសកម្ពុជា ដែលមានសាច់ជ្រូកអាំងដុតឱ្យល្អឥតខ្ចោះ និងបម្រើលើបាយចំហុយ។ សាច់​ជ្រូក​មាន​រសជាតិ​ឈ្ងុយ ផ្អែម​បន្តិច និង​មាន​ក្លិន​ឈ្ងុយ ដែល​ធ្វើ​ឱ្យ​វា​ជា​អាហារ​ដែល​ផ្តល់​ផាសុកភាព និង​ពេញចិត្ត។ ម្ហូបនេះត្រូវបានអមដោយបន្លែជ្រក់ និងទំពាំងបាយជូរស្រាលៗ ដើម្បីរក្សាតុល្យភាពរសជាតិ។ វាសាមញ្ញ តែសំបូរទៅដោយរសជាតិប្រពៃណីខ្មែរ។',
      'ingredient': [
        {
          'id': 112,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZR6XmYagigMKMTt1yIm8JNoaGv0w36RI6rQ&s',
          'ingredient_name': 'ខ្ទឹម'
        },
        {
          'id': 113,
          'ingredient_image': 'https://cdn.sabay.com/cdn/media.sabay.com/media/TECH-KK/SOVATH/Sep-2020-07/5f97de48d359a_1603788360_medium.jpg',
          'ingredient_name': 'ទឹកដោះគោ'
        },
        {
          'id': 114,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzKl35ryMt7obQ5kQ5Nn0zl_ArOSQhHVXXrQ&s',
          'ingredient_name': 'ទឹកត្រី'
        },
        {
          'id': 115,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoNO4CnBRnnHVkijwTh8f8bceZ9_6F5jGcfA&s',
          'ingredient_name': 'ស្ករត្នោត'
        },
        {
          'id': 116,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq7Fmx0kzBzryI1qGbs1PLiYzs5VCsUl_lDQ&s',
          'ingredient_name': 'ទឹកស៊ីអ៊ីវ'
        },
        {
          'id': 117,
          'ingredient_image': 'https://oss6.tnaot.com/tnaot/image/2022/08/06/75bbaf8ccf8c4457b334c81e854a3c3d.jpg',
          'ingredient_name': 'អង្ករសចំហុយ'
        },
        {
          'id': 118,
          'ingredient_image': 'https://oss6.tnaot.com/tnaot/image/2022/09/28/7e2b26ba87fa41e5968b72e82b3bfb1c.jpg',
          'ingredient_name': 'បន្លែជ្រក់'
        },
        {
          'id': 119,
          'ingredient_image': 'https://s4.kh1.co/__image/w=1200,h=630,q=100/c6/c6244ab472737db838aaa0ccc7f62a906aae382c.jpg',
          'ingredient_name': 'ទំពាំងបាយជូរឬស៊ុប'
        },
      ],
      'video': {
        'video_cooking': 'https://youtu.be/sa0inXURh90?si=BxLCPFD1qKa60zos',
        'receipe': 'ដើម្បីធ្វើបាយសាច់ជ្រូក (សាច់ជ្រូក និងបាយ) ដាក់សាច់ជ្រូកហាន់ជាបន្ទះស្តើងៗ ខ្ទឹមក្រហម ទឹកដោះគោ ទឹកត្រី ស្ករត្នោត និងទឹកស៊ីអ៊ីវ ដុតឲ្យម៉ដ្ឋ រួចដាក់អង្ករសចំហុយជាមួយបន្លែជ្រក់ និងទឹកស៊ុបមួយចំហៀង',
      }
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
      'food_image': 'https://huunghivietnamcampuchia.thoidai.com.vn/stores/news_dataimages/huunghivietnamcampuchia-thoidai-com-vn/092020/17/15/fn-2020-09-17-12-00-46-020210111140811.9412520.jpg',
      'food_image': 'https://huunghivietnamcampuchia.thoidai.com.vn/stores/news_dataimages/huunghivietnamcampuchia-thoidai-com-vn/092020/17/15/fn-2020-09-17-12-00-46-020210111140811.9412520.jpg',
      'food_name': 'នំអន្សមចេក',
      'food_name_english': 'Banana cake',
      'description': 'នំអន្សមចេក ជា​បង្អែម​ប្រពៃណី​ខ្មែរ​ដែល​ធ្វើ​ពី​អង្ករ​ដំណើប ចេក និង​ដូង។ វាជាអាហារដ៏ពេញនិយម ជាពិសេសក្នុងឱកាសចូលឆ្នាំខ្មែរ និងឱកាសពិសេសផ្សេងៗ។ បង្អែម​ត្រូវ​បាន​រុំ​ដោយ​ស្លឹក​ចេក រួច​ចំហុយ​ឲ្យ​បាន​គ្រប់​លក្ខណៈ។ ការរួមផ្សំនៃចេកផ្អែមជាមួយនឹងអង្ករដំណើប និងដូងសម្បូរបែប ធ្វើឱ្យវាក្លាយជាបង្អែមដែលមានរសជាតិ និងពេញចិត្ត។',
      'ingredient': [
        {
          'id': 120,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdbij0U72e0kvLHLjZCOVUpxcjzu07aFy_RQ&s',
          'ingredient_name': 'អង្ករដំណើប'
        },
        {
          'id': 121,
          'ingredient_image': 'https://cdn.cambonomist.com/media/images/banana-pixabay.2e16d0ba.fill-960x540.jpg',
          'ingredient_name': 'ចេកទុំ'
        },
        {
          'id': 122,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWhIvd2fPvLSq1vd7NA8xsFctpZp4oLkXNjQ&s',
          'ingredient_name': 'ខ្ទិះដូង'
        },
        {
          'id': 123,
          'ingredient_image': 'https://lareine.com.kh/wp-content/uploads/2020/08/La-Reine-01235.jpg',
          'ingredient_name': 'ស្ករត្នោត'
        },
        {
          'id': 124,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrSORHZQ8lNx4Q1UyvUH8xvwM7Mb-K0WzMYA&s',
          'ingredient_name': 'ស្លឹកចេក'
        },
      ],
      'video': {
        'video_cooking': 'https://youtu.be/6N7Wp1T7l7U?si=ajpkKyGPFyopNxtY',
        'receipe': 'ដើម្បីធ្វើនំអន្សមចេក លាយអង្ករដំណើបជាមួយខ្ទិះដូង និងស្ករស រុំចេកទុំក្នុងល្បាយដោយប្រើស្លឹកចេក បិទឱ្យជិត ចំហុយរហូតទាល់តែឆ្អិន រួចទទួលទានអាហារខ្មែរដ៏ផ្អែមនេះ។',
      }
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
      'food_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBftPEdIqANix2WyctJx-raBLNWLQXztS2hw&s',
      'food_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBftPEdIqANix2WyctJx-raBLNWLQXztS2hw&s',
      'food_name': 'ចេកខ្វិះ',
      'food_name_english': 'banana dessert',
      'description': 'ចេកខ្វិះ ជា​បង្អែម​ខ្មែរ​ពិសេស​មួយ​ដែល​មាន​ផ្លែ​ចេក​ក្នុង​ទឹក​ខ្ទិះដូង។ ចេក​ត្រូវ​បាន​ស្ងោរ​ក្នុង​ល្បាយ​ទឹកដោះគោ​ដូង​ដែល​មាន​រសជាតិ​ផ្អែម​ឆ្ងាញ់ ដែល​មនុស្ស​ជា​ច្រើន​ចូលចិត្ត ជាពិសេស​នៅ​តាម​ជនបទ។ វា​ជា​បង្អែម​ដ៏​សាមញ្ញ ប៉ុន្តែ​មាន​រសជាតិ​ឆ្ងាញ់ ដែល​ផ្តល់​នូវ​តុល្យភាព​ដ៏​ល្អឥតខ្ចោះ​នៃ​ភាពផ្អែម និង​ភាពសម្បូរបែប។',
      'ingredient': [
        {
          'id': 125,
          'ingredient_image': 'https://cdn.cambonomist.com/media/images/banana-pixabay.2e16d0ba.fill-960x540.jpg',
          'ingredient_name': 'ចេកទុំ'
        },
        {
          'id': 126,
          'ingredient_image': 'https://cdn.sabay.com/cdn/media.sabay.com/media/TECH-KK/SOVATH/Sep-2020-07/5f97de48d359a_1603788360_medium.jpg',
          'ingredient_name': 'ទឹកដោះគោ'
        },
        {
          'id': 127,
          'ingredient_image': 'https://sokhakrom.com/prms/uploads/plants/Capturekkl.PNG',
          'ingredient_name': 'ដូង'
        },
        {
          'id': 128,
          'ingredient_image': 'https://lareine.com.kh/wp-content/uploads/2020/08/La-Reine-01235.jpg',
          'ingredient_name': 'ស្ករត្នោត'
        },
        {
          'id': 129,
          'ingredient_image': 'https://www.knongsrok.com/wp-content/uploads/2023/03/1_4359b510-332d-417c-8e76-30f9c2d10508_480x480.webp',
          'ingredient_name': 'អំបិលមួយក្តាប់'
        },
      ],
      'video': {
        'video_cooking': 'https://youtu.be/lzjQbwzoPrc?si=pvqpxnG2y3PUDsVr',
        'receipe': 'ដើម្បី​ធ្វើ​ចេកខ្វិះ ត្រូវ​យក​ចេក​ទុំ​ដាក់​ក្នុង​ទឹកដោះគោ​ដូង​ផ្អែម​ជាមួយ​ស្ករត្នោត និង​អំបិល​បន្តិច​រហូត​ដល់​ចេក​ទន់​ហើយ​ទឹកជ្រលក់​ឡើង​ក្រាស់ រួច​យក​ទៅ​ធ្វើ​ជា​បង្អែម​ខ្មែរ​បែប​ក្តៅ​ៗ ។'
      }
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
      'food_image': 'https://images.deliveryhero.io/image/fd-kh/LH/xg31-hero.jpg?width=512&height=384&quality=45',
      'food_image': 'https://images.deliveryhero.io/image/fd-kh/LH/xg31-hero.jpg?width=512&height=384&quality=45',
      'food_name': 'គុយទាវ',
      'food_name_english': 'Noodles',
      'description': 'គុយទាវ គឺជាគុយទាវដ៏ពេញនិយមរបស់ខ្មែរ ដែលតែងតែបម្រើជាអាហារពេលព្រឹក ប៉ុន្តែអាចទទួលទានបានគ្រប់ពេលនៃថ្ងៃ។ ស៊ុប​នេះ​ត្រូវ​បាន​ផលិត​ឡើង​ដោយ​ទឹក​ទំពាំងបាយជូរ​ស្រាល និង​មាន​ក្លិន​ឈ្ងុយ ដែល​ជា​ធម្មតា​មាន​រសជាតិ​ជាមួយ​នឹង​សាច់មាន់ សាច់ជ្រូក ឬ​សាច់គោ ហើយ​តុបតែង​ដោយ​ឱសថ​ស្រស់ កំបោរ និង​ម្ទេស។ វា​ជា​ម្ហូប​ដែល​មាន​ផាសុកភាព និង​មាន​ច្រើន​មុខ​ដែល​ប្រជាជន​កម្ពុជា​ជាច្រើន​ចូលចិត្ត។',
      'ingredient': [
        {
          'id': 130,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyQsHB8o1MGWxJGKIt-IkZ9KNyOHbVPhCf_g&s',
          'ingredient_name': 'គុយទាវ'
        },
        {
          'id': 131,
          'ingredient_image': 'https://imagevietnam.vnanet.vn//MediaUpload/Org/2022/12/30/0130-9-28-18.jpg',
          'ingredient_name': 'សាច់គោ'
        },
        {
          'id': 132,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZR6XmYagigMKMTt1yIm8JNoaGv0w36RI6rQ&s',
          'ingredient_name': 'ខ្ទឹម'
        },
        {
          'id': 133,
          'ingredient_image': 'https://www.health.com.kh/wp-content/uploads/2023/01/image-5-2.jpg',
          'ingredient_name': 'ខ្ទឹមបារាំង'
        },
        {
          'id': 134,
          'ingredient_image': 'https://lh6.googleusercontent.com/proxy/L3ARqgH8Y22E8y7Tk33Q3QC3Tr3gELdy2Ah2JVk1EYVUGHef1XW-hUQXmgg7G37h0_9qbwYBu9toH5xYP4n3prV0uwoav3janpCEBbATebdGqGtSdcPeQJebICXxXDQxUA',
          'ingredient_name': 'ស្លឹកគ្រៃ'
        },
        {
          'id': 135,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzKl35ryMt7obQ5kQ5Nn0zl_ArOSQhHVXXrQ&s',
          'ingredient_name': 'ទឹកត្រី'
        },
        {
          'id': 136,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_N6P1f6q2aSDVQFLt8jLN4pcnoj9fRBV5EQ&s',
          'ingredient_name': 'អំបិលនិងស្ករ'
        },
        {
          'id': 137,
          'ingredient_image': 'https://thekhmerpress.com/wp-content/uploads/2021/11/t-09-Thai-Ministry-of-Commerce-addressing-issue-of-expensive-vegetables.jpeg',
          'ingredient_name': 'ជីវ៉ាន់ស៊ុយថៃ ជីអង្កាម'
        },
        {
          'id': 138,
          'ingredient_image': 'https://tokke.kesspay.io/storage/product/47635/hB4Hedqgff4iZcmzFzkEjuN8Ete7J2j76tgZuSO7.jpeg',
          'ingredient_name': 'ក្រូចឆ្មារ'
        },
        {
          'id': 139,
          'ingredient_image': 'https://economy.ams.com.kh/wp-content/uploads/2021/06/photo_2021-06-04_16-54-48.jpg',
          'ingredient_name': 'ម្ទេស'
        },
        {
          'id': 140,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZR6XmYagigMKMTt1yIm8JNoaGv0w36RI6rQ&s',
          'ingredient_name': 'ខ្ទឹម​ស'
        },
      ],
      'video': {
        'video_cooking': 'https://youtu.be/DVVaBGbSoYw?si=LGGgMIlLfblxRjOu',
        'receipe': 'ដើម្បី​ធ្វើ​គុយទាវ ត្រូវ​រៀបចំ​ទំពាំងបាយជូរ​រសជាតិ​ដោយ​ដាក់​សាច់មាន់ សាច់ជ្រូក ឬ​សាច់គោ​ជាមួយ​ខ្ទឹមស ខ្ទឹមបារាំង ស្លឹកគ្រៃ ទឹកត្រី អំបិល និង​ស្ករ​។ ចម្អិនគុយទាវដោយឡែកពីគ្នា បន្ទាប់មកដាក់គុយទាវចូលចានមួយ ចាក់ទឹកស៊ុបក្តៅៗពីលើ ហើយដាក់គ្រឿងក្រអូបស្រស់ ក្រូចឆ្មារ ខ្ទឹមក្រហម និងម្ទេសតាមការចង់បាន។',
      }
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
      'food_image': 'https://thukphadanet.wordpress.com/wp-content/uploads/2015/01/16-08-2014.jpg',
      'food_image': 'https://thukphadanet.wordpress.com/wp-content/uploads/2015/01/16-08-2014.jpg',
      'food_name': 'សម្លកកូ',
      'food_name_english': 'saml k kau',
      'ingredient': [
        {
          'id': 141,
          'ingredient_image': 'https://lh6.googleusercontent.com/proxy/L3ARqgH8Y22E8y7Tk33Q3QC3Tr3gELdy2Ah2JVk1EYVUGHef1XW-hUQXmgg7G37h0_9qbwYBu9toH5xYP4n3prV0uwoav3janpCEBbATebdGqGtSdcPeQJebICXxXDQxUA',
          'ingredient_name': 'ស្លឹកគ្រៃ'
        },
        {
          'id': 142,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQP7kOMlNEOlUSgh3bPqgeqz5D1ii2OmdHBsA&s',
          'ingredient_name': 'រមៀត'
        },
        {
          'id': 143,
          'ingredient_image': 'https://store24.kommong.com/wp-content/uploads/2021/05/%E1%9E%9F%E1%9E%B6%E1%9E%85%E1%9F%8B%E1%9E%87%E1%9F%92%E1%9E%9A%E1%9E%BC%E1%9E%803.jpg',
          'ingredient_name': 'សាច់ជ្រូក'
        },
        {
          'id': 144,
          'ingredient_image': 'https://tokke.kesspay.io/storage/product/48024/qYytbq1HVg1sTX4e5iQY1Av5MWJyDfR61HCU7DLU.jpeg',
          'ingredient_name': 'ម្សៅអង្ករលីង'
        },
        {
          'id': 145,
          'ingredient_image': 'https://lokbongrattanak.wordpress.com/wp-content/uploads/2018/02/img_6500.jpg?w=715&h=431',
          'ingredient_name': 'ពងទា'
        },
        {
          'id': 146,
          'ingredient_image': 'https://economy.ams.com.kh/wp-content/uploads/2024/05/Papa6.jpg',
          'ingredient_name': 'ផ្លែល្ហុងបៃតង'
        },
        {
          'id': 147,
          'ingredient_image': 'https://www.shuangxingseeds.com/uploads/HTB1rnEcKXOWBuNjy0Fiq6xFxVXaa.jpg',
          'ingredient_name': 'សណ្តែកវែង'
        },
        {
          'id': 148,
          'ingredient_image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Cucurbita_2011_G1.jpg/800px-Cucurbita_2011_G1.jpg',
          'ingredient_name': 'ល្ពៅ'
        },
        {
          'id': 149,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzKl35ryMt7obQ5kQ5Nn0zl_ArOSQhHVXXrQ&s',
          'ingredient_name': 'ទឹកត្រី'
        },
        {
          'id': 150,
          'ingredient_image': 'https://cdn.cambonomist.com/media/images/0b865671c0c3bf683aaf1bb110d500b7.2e16d0ba.fill-960x504.jpg',
          'ingredient_name': 'អំបិលនិងស្ករ'
        },
        {
          'id': 151,
          'ingredient_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzs_WtIpVuKg5Za4ql5eCoOztMXEvdI2S-Aw&s',
          'ingredient_name': 'ស្លឹកខ្ទឹម'
        },
      ],
       'video': {
        'video_cooking': 'https://youtu.be/nlsmzicLYis?si=3HO986d6wD-Dp-uc',
        'receipe': 'ដើម្បី​ធ្វើ​សម្លកកូ ត្រូវ​ប្រឡាក់​គ្រឿង​ក្រៀម​ក្នុង​ឆ្នាំង​រហូត​មាន​ក្លិន​ឈ្ងុយ រួច​ដាក់​សាច់ជ្រូក ឬ​ត្រី (បើ​ប្រើ) ហើយ​ចម្អិន​រហូត​ដល់​មាន​ពណ៌​ត្នោត​ស្រាល។ បន្ថែមទឹក ម្សៅអង្ករលីងអោយក្រាស់ រួចច្របល់ជាមួយទឹកត្រី អំបិល និងស្ករ។ បន្ថែមបន្លែ - ពងមាន់ ល្ហុងបៃតង សណ្តែកវែង និងល្ពៅ - ហើយដាំឱ្យពុះរហូតដល់ទន់។ បញ្ចប់ជាមួយនឹងឱសថស្រស់ៗដូចជា ស្លឹកខ្ទឹម និង basil ថៃមុនពេលបម្រើ។',
      }
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