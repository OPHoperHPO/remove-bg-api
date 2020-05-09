# 🍰 `remove-bg-api` - remove.bg Python API Wrapper 🍰
**********************************************************************
### 📄 Description:
This library is used to interact with the *remove.bg* API to remove the background from the image. \
**This library implements 100% API of this service.**
**********************************************************************
### 🧷 Dependencies:
```requests```
**********************************************************************
### 🔖 Setup:
#### 🏷 Simple install using pip:
`pip3 install remove-bg-api`
#### 🏷 Install from source:
* Clone this repository.
* Install all the dependencies from **requirements.txt**: ```pip3 install -r requirements.txt```
* Install ``python3 setup.py install``
**********************************************************************
### 📙 [Documentation](https://ophoperhpo.github.io/remove-bg-api/)
**********************************************************************
### 🧰 Examples:
* **Remove background from image:** 
    ```
    from remove_bg_api import RemoveBg
    # Initialize api wrapper
    removebg = RemoveBg(API_TOKEN)  
    # Send and save the finished image
    image = removebg.remove_bg_file(input_path="imgs/a.jpg", out_path="./a.png", size="preview", raw=False)  
    # Print path
    print("Image was saved along the path: {}".format(image))
    ```
* **Show account total balance:** 
    ```
    from remove_bg_api import RemoveBg
    removebg = RemoveBg("API_TOKEN")  # Initialize api wrapper
    print("Account total balance: ", removebg.account.balance())
    ```
**See other examples in the [examples](../master/examples/) folder.**
**********************************************************************
### ⏳ TODO:
```
1) Add asyncio support. (0% done)
```
### 💵 Support me:

You can thank me for developing this project, provide financial support for the development of new projects and buy me a small cup of coffee.☕\
  Just support me on these platforms: \
  ⭐[**Boosty**⭐](https://boosty.to/anodev) \
  ⭐[**DonationAlerts**⭐](https://www.donationalerts.com/r/anodev_development)
