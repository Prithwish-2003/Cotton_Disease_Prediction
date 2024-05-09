# Cotton_Disease_Prediction

# A deep learning model for cotton disease prediction using fine-tuning with smart web application in agriculture
- ## Abstract
Cotton is known as ‘white gold’ in the agricultural industry. Agriculture is the primary source of economic income in Bangladesh and the country's economy is heavily dependent on agriculture. The soil and water resources of our country are fertile and the climate is moderate. But numerous diseases affect crop production and cause enormous crop losses, endangering the lives of helpless farmers. A previous report showed that about 70–80% of cotton diseases were leaf diseases and 30–20% were pest diseases. Experts typically use bare eyes to find and identify such plant diseases and pests which may result from lower accuracy of the identification. As a result, early detection of cotton disease using AI-based systems may help to increase the production of cotton by detecting the leaf disease significantly. In this research, we proposed a DL-based cotton leaf disease detection approach using fine-tuning Transfer Learning (TL) algorithms by tuning the layers and parameters of the existing TL algorithms. We also investigated the performance of several fine-tuning TL model such as  Inception-V3  on the publicly available cotton dataset for cotton disease prediction. The investigations found that the Inception-V3 model provides the highest accuracy rate of 95% and was selected to develop a web-based smart application for real-life cotton disease prediction in farming to increase cotton production. Hence, our model can accurately diagnose cotton leaf diseases and will provide a new window for the automatic leaf disease diagnosis of other plants.

- Data link : [Data link](https://drive.google.com/drive/folders/1SfCipusCMqVd9a-0RLfBt_9JjCoIlfPi?usp=drive_link)
- ### Demo :
<img
  src="Demo/Screenshot (55).png"
  alt="Alt text"
  title="Cotton Disease title"
  style="display: inline-block; margin: 0 auto; max-width: 1000px">
## Workflow

1. update config.yaml
2. update secrets.yaml
3. update params.yaml
4. update the entity
5. update the configaration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml


## Git Command
```bash
git add .

git commit -m "first commit"

git push -u origin main
```




## How To Run -->
```bash
conda create -n venv python=3.8 -y
```

```bash
conda activate venv
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```




### loss and accuracy chart of model after training
```bash
	 loss       accuracy	val_loss	val_accuracy
0	2.885419	0.739108	0.123106	0.944444
1	0.659565	0.882472	0.036769	1.000000
2	0.510929	0.906282	0.001396	1.000000
3	0.601421	0.907801	0.147037	0.944444
4	0.462919	0.924519	0.315755	0.944444
5	0.490968	0.923506	0.061596	1.000000
6	0.354162	0.942249	0.543986	0.833333
7	0.327910	0.950861	1.745108	0.833333
8	0.373893	0.941236	0.126065	0.944444
9	0.601824	0.928571	0.000338	1.000000

```
