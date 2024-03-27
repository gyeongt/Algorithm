import torch
import torchvision
import torchvision.transforms as transforms


# 학습속도를 높이기 위해 gpu사용 여부
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

batch_size = 4
trainset = torchvision.datasets.ImageFolder(root='/Users/byeongyeongtae/Documents/archive/training_set/training_set', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)

testset = torchvision.datasets.ImageFolder(root='/Users/byeongyeongtae/Documents/archive/test_set/test_set', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=2)

classes = ('cat', 'dog',)

