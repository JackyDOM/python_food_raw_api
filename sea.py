from flask import jsonify

sea = [
  {
    'id': 1,
    'sea_name': 'កោះរ៉ុង',
    'sea_image': 'https://s9.kh1.co/__image/w=1200,h=630,q=100/97/97ada4a9557f35a7881d07e28ce2de0d72a7e00f.jpg',
    'deatil': {
      'sea_image': 'https://s9.kh1.co/__image/w=1200,h=630,q=100/97/97ada4a9557f35a7881d07e28ce2de0d72a7e00f.jpg',
      'sea_name': 'កោះរ៉ុង',
      'description': 'កោះរ៉ុង ជាកោះដ៏មានកេរ្តិ៍ឈ្មោះល្បីល្បាញដោយសារឆ្នេរខ្សាច់ស ទឹកថ្លាថ្លា និងជីវិតសមុទ្ររស់រវើក។ វាផ្តល់នូវការរត់គេចខ្លួនដ៏ស្ងប់ស្ងាត់ ល្អឥតខ្ចោះសម្រាប់ការហែលទឹក ស្រមុក និងសម្រាកនៅក្រោមព្រះអាទិត្យ។',
      'location': 'នៅឆ្នេរសមុទ្រខេត្តព្រះសីហនុ ប្រទេសកម្ពុជា។',
      'notableFeatures': 'ឆ្នេរឡុងសិត និងឆ្នេរសុខសានសម្រាប់ទេសភាពដ៏អស្ចារ្យរបស់ពួកគេ។ Plankton Phosphorescent ដែលអាចមើលឃើញនៅពេលយប់។ ការរួមបញ្ចូលគ្នានៃឆ្នេរស្ងប់ស្ងាត់ និងកន្លែងជប់លៀងដ៏រស់រវើក។',
    }
  },
  {
    'id': 2,
    'sea_name': 'ឆ្នេរកែប',
    'sea_image': 'https://www.visitkampot.info/__asset/img/article/60bd0899af997.jpg',
    'detail': {
      'sea_image': 'https://www.visitkampot.info/__asset/img/article/60bd0899af997.jpg',
      'sea_name': 'ឆ្នេរកែប',
      'description': 'ទីក្រុងមាត់សមុទ្រដ៏ទាក់ទាញមួយដែលមានបរិយាកាសសម្រាកកាយ កែបមានភាពល្បីល្បាញសម្រាប់អាហារសមុទ្រស្រស់ៗ ជាពិសេសក្តាម និងទិដ្ឋភាពថ្ងៃលិចដ៏គួរឱ្យភ្ញាក់ផ្អើលនៅលើឈូងសមុទ្រថៃ។',
      'location': 'ខេត្តកែប ជាប់ព្រំដែនកម្ពុជា-វៀតណាម។',
      'notableFeature': 'ផ្សារក្តាម ផ្តល់ជូនគ្រឿងសមុទ្រដែលចាប់បានថ្មីៗ។ ឧទ្យានជាតិកែបសម្រាប់ការឡើងភ្នំ និងទេសភាពបែប Panoramic ។ កោះទន្សាយ (កោះទន្សាយ) អាចចូលបានដោយជិះទូកខ្លី។'
    }
  },
  {
    'id': 3,
    'sea_name': 'ឆ្នេរអូត្រេស',
    'sea_image': 'https://kohsantepheapdaily.com.kh/wp-content/uploads/2015/2/ad192e46-c2ec-4f28-9feb-1d801de12702.jpg',
    'detail': {
      'sea_image': 'https://kohsantepheapdaily.com.kh/wp-content/uploads/2015/2/ad192e46-c2ec-4f28-9feb-1d801de12702.jpg',
      'sea_name': 'ឆ្នេរអូត្រេស',
      'description': 'ឆ្នេរអូត្រេស ជាឆ្នេរដ៏ស្រស់បំព្រងដែលមានខ្សាច់ពណ៌មាស និងទឹកស្ងប់ស្ងាត់ ឆ្នេរអូត្រេសគឺល្អសម្រាប់អ្នកដែលស្វែងរកកន្លែងលំហែកាយដោយសន្តិភាព។ វាផ្តល់ជូនទាំងការស្នាក់នៅបែបថវិកា និងការស្នាក់នៅខ្ពស់។',
      'location': 'ជិតក្រុងព្រះសីហនុ ប្រទេសកម្ពុជា។',
      'notableFeature': 'ទិដ្ឋភាពថ្ងៃលិច និងភោជនីយដ្ឋាននៅមាត់សមុទ្រ។ សកម្មភាពក្នុងទឹកដូចជា ជិះក្តារប៉ាយ និងកាយ៉ាកជាដើម។ ផ្សាររាត្រីអូរត្រេះ ដែលមានតន្ត្រីផ្សាយបន្តផ្ទាល់ និងទំនិញសិល្បៈ។',
    }
  },
  {
    'id': 4,
    'sea_name': 'កោះរ៉ុងសន្លឹម',
    'sea_image': 'https://3.bp.blogspot.com/-tBkiihUV94Y/W4T-d69NWhI/AAAAAAAALvk/pVvFaOt26NsdXbyoMFnY1SW1A1zg86rxACLcBGAs/s1600/54060913.jpg',
    'detail': {
      'sea_image': 'https://3.bp.blogspot.com/-tBkiihUV94Y/W4T-d69NWhI/AAAAAAAALvk/pVvFaOt26NsdXbyoMFnY1SW1A1zg86rxACLcBGAs/s1600/54060913.jpg',
      'sea_name': 'កោះរ៉ុងសន្លឹម',
      'description': 'កោះរ៉ុងដ៏ស្ងប់ស្ងាត់ និងស្ងប់ស្ងាត់ជាងនេះ កោះនេះគឺល្អឥតខ្ចោះសម្រាប់ការសម្រាកលំហែ ផ្តល់នូវឆ្នេរស្ងប់ស្ងាត់ និងព្រៃខៀវស្រងាត់។',
      'location': 'នៅឆ្នេរសមុទ្រខេត្តព្រះសីហនុ ប្រទេសកម្ពុជា។',
      'notableFeature': 'Saracen Bay សម្រាប់ទឹកស្ងប់ស្ងាត់ និងបឹងហ្គាឡូនៅមាត់សមុទ្រ។ កន្លែងមុជទឹកជាមួយផ្កាថ្មដ៏រស់រវើក។ ឆ្នេរ Sunset ដែលត្រូវបានគេស្គាល់ថាសម្រាប់ថ្ងៃលិចដ៏អស្ចារ្យរបស់វា។',
    }
  },
  {
    'id': 5,
    'sea_name': 'ឧទ្យានជាតិរាម',
    'sea_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRM-4tm5n3FlIkFs10DUTSUS2UwLVYN7mm_g&s',
    'detail': {
      'sea_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRM-4tm5n3FlIkFs10DUTSUS2UwLVYN7mm_g&s',
      'sea_name': 'ឧទ្យានជាតិរាម',
      'description': 'ឧទ្យានជាតិឆ្នេរមួយដែលមានប្រព័ន្ធអេកូឡូស៊ីចម្រុះ រួមមានព្រៃកោងកាង ឆ្នេរ និងកោះនៅឆ្នេរសមុទ្រ។ វាជាជម្រកសម្រាប់អ្នកស្រឡាញ់សត្វព្រៃ និងធម្មជាតិ។',
      'location': 'ជិតក្រុងព្រះសីហនុ ប្រទេសកម្ពុជា។',
      'notableFeature': 'ដំណើរកម្សាន្តតាមទូកឆ្លងកាត់ព្រៃកោងកាង និងមាត់ទន្លេ។ ការមើលសត្វស្លាប និងប្រទះឃើញប្រភេទសត្វកម្រដូចជាឆ្មានេសាទ។ ឆ្នេរស្អាត និងផ្លូវដើរកាត់ព្រៃខៀវស្រងាត់។',
    }
  }
]

def get_sea():
  response = {
        "status": 200,
        "message": "sea retrieved successfully",
        "data": sea,
    }
  return jsonify(response)